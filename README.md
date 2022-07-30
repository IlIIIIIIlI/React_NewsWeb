# React Project: A news web

## Hi, welcome to Andy yang's Web project.

The project using python bs4 to sraping info from a news website. then the info updates the django's SQLite database. I held the django in a AWS with OS ubantu, here is the link for [config EC2](https://www.youtube.com/watch?v=zfOQ7OA52tM). Make sure the region is run nearest to you.

- get a domain and write the [certificate](https://ap-southeast-2.console.aws.amazon.com/acm/home?region=ap-southeast-2#/certificates/list) to the [Route53](https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones#ListRecordSets/Z05858652FRJ2KEG31LQC)
- update the django running server, make it a [https](https://stackoverflow.com/questions/8023126/how-can-i-test-https-connections-with-django-as-easily-as-i-can-non-https-connec). (this is actually not the best way, but at least to run it)
  - Alternative ways: [install SSL](https://www.youtube.com/watch?v=dYdv6pkCufk&t=167s), [Certbot](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04)
  - the web has warning of your browser said insecure, that's doesn't matter. as long as you have AWS certificate for your domain.

My React app reads the django's api, then return the data.

Here's link for the web project: https://deft-donut-b7ce6e.netlify.app/

and this is the link for backend: https://backendapicall.click:8000/api/news

## for the netlify

- npm run build
- copy the build folder directly to make the web.



## some React refs

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
