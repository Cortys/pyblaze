import math
import torch

def log_prob_standard_normal(x):
    """
    Computes the log-probability of observing the given data under a (multivariate) standard Normal
    distribution. Although this function is equivalent to the :code:`log_prob` method of the
    :class:`torch.distributions.MultivariateNormal` class, this implementation is much more
    efficient due to the restriction to standard Normal.

    Parameters
    ----------
    x: torch.Tensor [N, D]
        The samples whose log-probability shall be computed (number of samples N, dimensionality D).

    Returns
    -------
    torch.Tensor [N]
        The log-probabilities for all samples.
    """
    dim = x.size(1)
    const = dim * math.log(2 * math.pi)
    norm = torch.einsum('ij,ij->i', x, x)
    return -0.5 * (const + norm)
