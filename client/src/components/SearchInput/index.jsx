import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Box, Button, Input } from "@chakra-ui/react";
import { FaArrowUp } from "react-icons/fa6";

const SearchInput = ({ handleClick }) => {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
    // console.log("Message:", inputValue);
    handleClick(inputValue);
  };

  return (
    <Box
     border={'2px'}
     borderColor={'gray.400'}
     w={'100%'}
     py={'0.5rem'}
     px={'0.5rem'}
     borderRadius={'1rem'}
     display={'flex'}
    >
        <Input 
          variant={'unstyled'} 
          placeholder={'Message FirstAid...'} 
          value={inputValue} 
          onChange={handleChange} 
        />
        <Button onClick={handleButtonClick}><FaArrowUp /></Button>
    </Box>
  )
};

export default SearchInput;

SearchInput.propTypes = {
    handleClick: PropTypes.func,
};
