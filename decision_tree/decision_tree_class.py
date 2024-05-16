from __future__ import annotations

from dataclasses import dataclass
import numpy as np
import json
@dataclass
class Node:
    """
    A node in a decision tree.

    Parameters
    ----------
    feature : int, optional (default=None)
        The feature index used for splitting the node.
    threshold : float, optional (default=None)
        The threshold value at the node.
    n_samples : int, optional (default=None)
        The number of samples at the node.
    value : int, optional (default=None)
        The value of the node (i.e., the mean target value of the samples at the node).
    mse : float, optional (default=None)
        The mean squared error of the node (i.e., the impurity criterion).
    left : Node, optional (default=None)
        The left child node.
    right : Node, optional (default=None)
        The right child node.
    """

    feature: int = None
    threshold: float = None
    n_samples: int = None
    value: int = None
    mse: float = None
    left: Node = None
    right: Node = None


@dataclass
class DecisionTreeRegressor:
    """Decision tree regressor."""

    max_depth: int
    min_samples_split: int = 2

    def fit(self, X: np.ndarray, y: np.ndarray) -> DecisionTreeRegressor:
        """Build a decision tree regressor from the training set (X, y).

        Parameters:
        X (np.ndarray): The input features.
        y (np.ndarray): The target values.

        Returns:
        DecisionTreeRegressor: The fitted decision tree regressor.
        """
        self.n_features_ = X.shape[1]
        self.tree_ = self._split_node(X, y)
        return self

    def _mse(self, y: np.ndarray) -> float:
        """Compute the mean squared error of a vector.

        Parameters:
        y (np.ndarray): The input vector.

        Returns:
        float: The mean squared error.
        """
        return np.mean((y - np.mean(y)) ** 2)

    def _weighted_mse(self, y_left: np.ndarray, y_right: np.ndarray) -> float:
        """Compute the weighted mean squared error of two vectors.

        Parameters:
        y_left (np.ndarray): The left vector.
        y_right (np.ndarray): The right vector.

        Returns:
        float: The weighted mean squared error.
        """
        mse_l = self._mse(y_left)
        mse_r = self._mse(y_right)
        size_left = y_left.shape[0]
        size_right = y_right.shape[0]
        return (mse_l * size_left + mse_r * size_right)/(size_left + size_right)

    def _best_split(self, X: np.ndarray, y: np.ndarray) -> tuple[int, float]:
        """Find the best split for a node.

        Parameters:
        X (np.ndarray): The input features.
        y (np.ndarray): The target values.

        Returns:
        tuple[int, float]: The best feature index and threshold.
        """
        if np.unique(y).size == 1 or X.shape[0] < self.min_samples_split:
            return None, None
        feature_best, threshold_best, mse_best = None, None, float("inf")
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left = y[X[:, feature] <= threshold]
                right = y[X[:, feature] > threshold]
                if left.size == 0 or right.size == 0:
                    continue
                mse = self._weighted_mse(left, right)
                if mse < mse_best:
                    mse_best = mse
                    threshold_best = threshold
                    feature_best = feature
        return feature_best, threshold_best

    def _split_node(self, X: np.ndarray, y: np.ndarray, depth: int = 0) -> Node:
        """Split a node and return the resulting left and right child nodes.

        Parameters:
        X (np.ndarray): The input features.
        y (np.ndarray): The target values.
        depth (int): The current depth of the tree.

        Returns:
        Node: The resulting node after splitting.
        """
        node = Node(n_samples=X.shape[0], value = int(np.round(np.mean(y))), mse=self._mse(y))
        if depth >= self.max_depth:
            return node
        feature_best, threshold_best = self._best_split(X, y)
        if feature_best is None:
            return node
        node.feature = feature_best
        node.threshold = threshold_best
        left = X[:, feature_best] <= threshold_best
        node.left = self._split_node(X[left], y[left], depth + 1)
        node.right = self._split_node(X[~left], y[~left], depth + 1)
        return node

    def as_json(self) -> str:
        """Return the decision tree as a JSON string."""
        json_string = json.dumps(self._as_json(self.tree_))
        return json_string

    def _as_json(self, node: Node) -> str:
        """Return the decision tree as a JSON string. Execute recursively."""

        if node.left is None:
            json_dict = {
            "value" : node.value,
            "n_samples": node.n_samples,
            "mse": np.round(node.mse,2)
            }
        else:
            json_dict = {
            "feature": node.feature,
            "threshold": node.threshold.item(),
            "n_samples": node.n_samples,
            "mse": np.round(node.mse,2),
            "left" : self._as_json(node.left),
            "right" : self._as_json(node.right)
            }
        return json_dict
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict regression target for X.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input samples.

        Returns
        -------
        y : array of shape (n_samples,)
            The predicted values.
        """
        if X[0].shape:
            return [self._predict_one_sample(x) for x in X]
        else:
            return self._predict_one_sample(X)


    def _predict_one_sample(self, features: np.ndarray) -> int:
        """Predict the target value of a single sample."""
        current_node = self.tree_
        while current_node.left is not None:
            if features[current_node.feature] <= current_node.threshold:
                current_node = current_node.left
            else:
                current_node = current_node.right
        ans = current_node.value
        return ans
