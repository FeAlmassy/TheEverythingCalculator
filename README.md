# TEC — The Everything Calculator

A collection of mathematical models implemented from first principles —
portfolio optimization, linear programming, genetic algorithms, Markov chains,
and whatever else comes next. Each module is built by hand before becoming a
library: derive, code in pure Python, then accelerate.

The platform is a multi-page web application written in FastAPI, deployed on
a Hetzner Cloud server. Each model lives in its own repository and is consumed
here as an installable Python package.

## Modules

| Module                                                                  | Status      | Description                                       |
|-------------------------------------------------------------------------|-------------|---------------------------------------------------|
| [Portfolio_Optimizer](https://github.com/FeAlmassy/Portfolio_Optimizer) | in refactor | Vectorized mean–variance optimization in NumPy    |
| Abate_Optimizer                                                         | planned     | Linear programming applied to cattle slaughter    |
| CredituS                                                                | planned     | Genetic algorithm for credit risk classification  |

## Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn
- **Templating:** Jinja2
- **Frontend:** static HTML + minimal CSS, no JavaScript framework
- **Deployment:** systemd on Hetzner Cloud (Ubuntu)

## Author

Fellipe Almässy — applied mathematician, currently completing a Computer
Engineering degree at UAM (São Paulo). Trajectory: data science → ITA master's
in operations research → NATO SAS panel, applied mathematics for defense.

[github.com/FeAlmassy](https://github.com/FeAlmassy)
