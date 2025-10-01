# 🚀 JetSetGo
*A comprehensive software suite for analysis and design of full-scale, multi-stage launch vehicle systems.*

---
## ⚡ How to Run JetSetGo
1. **Create a virtual environment** (optional but recommended)  
   ```
    python -m venv .venvJSG
   ```
1. **Activate** (optional but recommended)  
    ```
    .venvJSG\Scripts\activate
    ```
Follow these steps to set up and run the minimal JetSetGo CLI to spawn a Single JET:
1. ```pip install --upgrade pip setuptools wheel``
1. ```pip install .```
1. ```jetsetgo```
---
Follow these steps to spawn a Multiple JETs
1. ```pip install .```
1. ```python spawn_jets.py```

## ✨ Features

### 1. Vehicle Configurator & Editor
1. Create and manage **multi-stage launch vehicles**.
1. Edit:
   1. Stage dry mass  
   1. Propellant and tank sizing  
   1. Engines & clustering  
   1. Payload definitions  
   1. Structural fractions  
   1. Avionics & fairings  
   1. Separation events  

---

### 2. Mass & Performance Budgets
1. Mass breakdowns for each subsystem.  
1. Δv per stage with **Tsiolkovsky’s rocket equation**.  
1. Gross mass, inert mass, and margin tracking.  
1. Center-of-gravity estimation.  

---

### 3. Propulsion Tools
1. Built-in **engine database**.  
1. Thrust & Isp performance vs. altitude and mixture ratio.  
1. Throttling models for flexible operations.  
1. Clustered engine support.  

---

### 4. Trajectory & Ascent Simulation
1. Configurable integrators:  
   1. **0D/1D/3DoF ascent** (6DoF coming soon).  
1. Atmosphere models with drag and gravity losses.  
1. Steering law support for guidance and control.  
1. Outputs:  
   1. Altitude vs. time  
   1. Velocity vs. altitude  
   1. Mass vs. time  

---

### 5. Aerodynamics
1. Simple aerodynamic coefficient models.  
1. Empirical curves and predictor models.  
1. User-specified coefficient tables.  

---

### 6. Staging & Separation Modeling
1. Define **stage separation events**.  
1. Fairing jettison logic.  
1. Residual propellant handling.  
1. Flexible staging timing.  

---

### 7. Optimization & Trade Studies
1. Tank sizing and stage optimization.  
1. **Multi-objective optimization**:  
   1. Maximize payload mass  
   1. Minimize cost  
   1. Improve reliability  
1. Monte Carlo uncertainty studies.  

---

### 8. Thermal & Environment Checks
1. Heating loads during ascent.  
1. Re-entry considerations (future scope).  
1. Structural **G-load tracking**.  

---

### 9. Cost & Reliability Models
1. Cost Estimating Relationships (**CERs**).  
1. Reliability models for:  
   1. Stages  
   1. Engines  
   1. Subsystems  

---

### 10. Reporting & Visualization
1. Interactive plots:  
   1. Mass breakdown pie chart  
   1. Δv ladder diagram  
   1. Ascent trajectory plots  
1. Export results to **PDF** and **CSV**.  
1. Share-ready visual outputs.  


### 11. Metric Units Reference

1. **Vehicle Configurator & Editor**
   1. Dry mass, propellant mass, payload mass → **kilograms (kg)**
   1. Tank volumes → **liters (L)** or **cubic meters (m³)**
   1. Stage dimensions → **meters (m)**
   1. Forces/thrust → **Newtons (N)**

1. **Mass & Performance Budgets**
   1. Δv per stage → **meters per second (m/s)**
   1. Gross/inert mass → **kg**
   1. Center-of-gravity → **meters from reference point**

1. **Propulsion Tools**
   1. ISP → **seconds (s)**
   1. Thrust → **N**
   1. Mass flow → **kg/s**

1. **Trajectory & Ascent Simulation**
   1. Altitude → **meters (m)**
   1. Velocity → **m/s**
   1. Acceleration → **m/s²**
   1. Time → **seconds (s)**

1. **Aerodynamics**
   1. Drag coefficient (dimensionless)
   1. Atmospheric density → **kg/m³**
   1. Reference areas → **m²**

1. **Thermal & Environment Checks**
   1. Temperature → **Kelvin (K)** or **°C**
   1. Heat flux → **W/m²**

1. **Cost & Reliability Models**
   1. Cost → can remain in **USD** or local currency
   1. Mass fractions remain dimensionless ratios


## ✨ Project Structure
- launch_vehicle_app/
  - app.py                 # Main entrypoint
  - config.py              # Global settings/config
  - core/                  # Core modules for vehicle modeling and simulation
    - __init__.py
    - propulsion.py        # Propulsion modeling (engines, ISP, thrust curves)
    - aerodynamics.py      # Drag, lift, stability analysis
    - structures.py        # Structural mass & load calculations
    - staging.py           # Multi-stage performance
    - trajectory.py        # Ascent trajectory simulation
    - optimization.py      # Stage optimization, payload maximization
  - data/                  # Input/output data
    - vehicle_configs/     # Example JSON/YAML vehicle configurations
    - results/             # Output files (CSV, JSON, plots)
  - utils/                 # Utility/helper modules
    - __init__.py
    - math_helpers.py      # Common equations
    - plotting.py          # Matplotlib/Plotly visualizations
    - fileio.py            # Read/write configs & results

## Author
Developed by [Praketa Saxena](https://github.com/kethsaxena)

## Last Edit
_Last updated: 27 Sep 2025
