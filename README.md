# Make-shift_Manipulator
A simple manipulator that works based on inverse kinematics done in MATLAB which is then sent to Raspberry-Pi through ROS 


INSTRUCTIONS -- to run the simulation

Step 1 >> Copy the Config , Scripts , Urdf and launch folders from  "/Make-shift_Manipulator/workspace_master/src/msm_master " into your ROS package.

step 2 >> Modify the arm_gazebo.launch inside the launch folder by replaceing all occurences of msm_master by your package name then run catkin_make once in the terminal .

step 3 >> finally run  roslaunch your_package_name arm_gazebo.launch



Instructions -- to run the controller

for now the matlab inverse kinematics control part has not been uploaded but a simple form of control is available
just run rosrun your_package_name 2cylmove.py     (if it dosen't run make sure it is an executable by running chmod +x 2cylmove in the terminal  when in the directory containing the file)  
 
