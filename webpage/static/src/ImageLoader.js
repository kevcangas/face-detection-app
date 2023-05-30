import axios from 'axios';

import React, { Component, useState } from 'react';

import { Visor } from './Visor';

class ImageLoader extends Component {


	state = {

		// Initially, no file is selected
		selectedFile: null,
        image: null
	};

	// On file select (from the pop up)
	onFileChange = event => {

		// Update the state
		this.setState({ selectedFile: event.target.files[0] });

	};

	// On file upload (click the upload button)
	onFileUpload = () => {

		// Create an object of formData
		const formData = new FormData();

		// Update the formData object
		formData.append(
			"file",
            this.state.selectedFile
			//this.state.selectedFile
			
		);
        
        //console.log(this.state.selectedFile);
		// Details of the uploaded file
		console.log(this.state.selectedFile);

		// Request made to the backend api
		// Send formData object
        const headers={'Content-Type': 'multipart/form-data'}
		axios.post("http://127.0.0.1:8000/imagefaces/", formData, headers)
        .then((response)=>{
            console.log(response);
            this.setState({ image:response.data.detail.image })
        })
	};

	// File content to be displayed after
	// file upload is complete
	fileData = () => {

		if (this.state.selectedFile) {

			return (
				<div>
					<h2>File Details:</h2>
					<p>File Name: {this.state.selectedFile.name}</p>

					<p>File Type: {this.state.selectedFile.type}</p>

					<p>
						Last Modified:{" "}
						{this.state.selectedFile.lastModifiedDate.toDateString()}
					</p>


				</div>
			);
		} else {
			return (
				<div>
					<br />
					<h4>Choose before Pressing the Upload button</h4>
				</div>
			);
		}
	};

	render() {

        var visor
        if (this.state.image != null){
            visor = <Visor image={this.state.image}></Visor>
        }
        else {
            visor = <h1>No image uploaded!</h1>
        }
		return (
			<div>
				<h1>
					GeeksforGeeks
				</h1>
				<h3>
					File Upload using React!
				</h3>
				<div>
					<input type="file" onChange={this.onFileChange} />
					<button onClick={this.onFileUpload}>
						Upload!
					</button>
				</div>
				{this.fileData()}
                {visor}
                
                
			</div>
		);
	}
}

export { ImageLoader }