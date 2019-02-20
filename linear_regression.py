#Script for Linear Regression in Python
#Code learned in CodeCademy lessons

#Function to find the gradient of b at every point
def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
      y_val = y[i]
      x_val = x[i]
      diff += (y_val - ((m * x_val) + b))
    b_gradient = -2/N * diff
    return b_gradient

#Function to find the m gradient at every point
def get_gradient_at_m(x, y, m, b):
  diff = 0
  N = len(x)
  for i in range(N):
    y_val = y[i]
    x_val = x[i]
    diff += (x_val * (y_val - (m * x_val + b)))
  m_gradient = (-2/N) * diff
  return m_gradient

#Your step_gradient function here
def step_gradient(x, y, b_current, m_current):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b = b_current - (0.01 * b_gradient)
    m = m_current - (0.01 * m_gradient)
    return [b, m]
