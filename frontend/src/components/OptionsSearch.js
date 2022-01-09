import React from 'react'; 
import { ToggleButton } from '@mui/material';

const OptionsSearch = (options) => {

    return (
        <ToggleButtonGroup
            color="primary"
            value={alignment}
            exclusive
            onChange={handleChange}
        >
            {options.map(option => (<ToggleButton value={options.value}>{option.text}</ToggleButton>))}
        </ToggleButtonGroup>
    )
}