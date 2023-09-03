// Connect to ROS2 WebSocket bridge
const ros = new ROSLIB.Ros({
        url: 'ws://localhost:9090' // Replace with your ROS2 WebSocket bridge URL
    });
    
    ros.on('connection', () => {
        console.log('Connected to ROS2 WebSocket');
    });
    
    ros.on('error', (error) => {
        console.error('Error connecting to ROS2 WebSocket:', error);
    });
    
    ros.on('close', () => {
        console.log('Connection to ROS2 WebSocket closed');
    });
    
    // Define a publisher for sending numbers to a topic
    const numberTopic = new ROSLIB.Topic({
        ros: ros,
        name: '/web_commands', // Replace with your desired topic name
        messageType: 'std_msgs/Int32' // Adjust the message type as needed
    });
    
    // Example: Publish a random number when the button is clicked
    const publishButton = document.getElementById('publishButton');
    publishButton.addEventListener('click', () => {
        const randomNumber = Math.floor(Math.random() * 100); // Generate a random number
        const message = new ROSLIB.Message({
            data: randomNumber
        });
        numberTopic.publish(message);
        console.log('Published:', randomNumber);
    });
    