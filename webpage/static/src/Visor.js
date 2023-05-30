import React, { Component, useRef } from 'react'

import './Visor.css';

class Visor extends Component {
    
    componentDidMount() {
        
        //console.log(this.props.image)
        if (this.props.image != null){
            const img_to_show = document.querySelector('img')
            
            var img_d
            img_d = 'data:image/png;base64,' + this.props.image
            
            img_to_show.src=img_d
           
        }
    }
    
    render() {
        return(
            <img src=""/>
        )
    }
}

export { Visor };