## MERN setup guide
1. Create a folder for your project: beltreviewer

2. beltReviewer (go into the project)

3. Initialize « javascript package for the project using: ```npm init -y```

4. install dependencies: ```npm install express cors mongoose```

5. Create a server.js file in the project folder  ```type nul > [filename]```

6. Create a server folder in the project folder

7. Make 4 directories in the server folder: config, models, controller, routes

8. Make a mongoose.configs.js file in the config folder

9. Set up the config.js file as usual—>make sure you change name of db to something unique thot you havent used yet

10. Set up server.js as usual (remember to require the mongoose config, don't require the routes yet b/c they hove not been created yet) ~ also remember the app.use() commands for post data!

11. CHECKPOINT-Test It using nodemon server.js (running the server) to make sure it says established connection with db

12. Create a model file as usual in the models folder. Set up model according to wireframe and project requirements.

13. Create a controller file in the controllers folder, and set up the controllers to work with your models that you imported-
Controller file needs the import to connect with the model. Have the crud functions in the controllers

14. Create a routes file in the routes folder and set up routes. import the controllers in the routes file. Make sure the methods in
the controllers are referenced in the routes

15. In servers.js import (require) the routes and pass the app object to it (make sure this is the second to last line in server js-
‘basicaly the require routes port is underneath the app.use parts)

16. CHECKPOINT: test all routes using postman before bulding the front end

17. Enable CORS-> in server.js Import it and then insert the app.use(cors()) command

18. Create a react app inside the project folder-> name it “client”

19 Install dependecies for react-> cd into folder and run "npm install axios react-router-dom"

20. Build out the front end!

