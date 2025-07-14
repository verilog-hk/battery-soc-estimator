Project Title: Battery State of Charge (SoC) Estimation using Coulomb Counting in MATLAB Simulink

Description: A brief overview of the project, highlighting the importance of SoC estimation and the chosen methodology (Coulomb Counting).

Features:

MATLAB Simulink-based simulation.

Real-time SoC tracking using current integration.

Dynamic load conditions (DC motor with torque).

Visualization of SoC, voltage, and current.

Methodology: Coulomb Counting

Explanation of the Coulomb Counting principle.

The formula used: 

SOC(t)=SOC(t−1)+
int_0 
t
 
fracIC_bat
cdotdt 

Breakdown of terms (

SOC(t), SOC(t−1), C_bat, I(t)) 

Discussion of considerations:

Accuracy of initial SOC 

Accumulation of measurement errors 

Sensitivity to sampling rate and noise 

Computational efficiency and ease of implementation 


System Design & Implementation (MATLAB Simulink)

Description of the Simulink model components (Battery block, DC Motor block, integrator, custom function, display blocks).



Explanation of how current is processed and integrated to calculate SoC.


Include an embedded image of your Simulink circuit diagram (Figure 1 and Figure 2 from your report).

Results and Discussion:

Summarize the key findings, including the initial and final SoC values.

Discuss the model's accuracy in tracking discharge and its practical applicability.


Mention the validation under dynamic load conditions.

Include an embedded image of your result (Figure 3 from your report).

How to Run the Simulation:

Instructions on opening and running the Simulink model.

Prerequisites (MATLAB with Simulink).

Future Enhancements: (Crucially, this addresses the "ML + Signal Filtering" aspect)

Integrating temperature effects.

Implementation with error correction techniques like Kalman Filters.

Exploring machine learning approaches for SoC estimation.

Extending the model to include battery aging and capacity fade.
