import { Box, Button, Flex, Image, Text, useToast } from "@chakra-ui/react"
import { useEffect, useState } from "react"
import TopNav from "../../components/TopNav"
import { useStore } from "../../hooks/useStore"
import distinguishGender from "../../utils/girlBoyFilter"
import Avatar from '../../assets/9334410.jpg'
import { useNavigate } from "react-router-dom"


const Profile = () => {
  const navigate = useNavigate()
  const toast = useToast()
  const firstAidUser = useStore((state) => state.user)
  const signOutUser = useStore((state) => state.signOutUser)

  const handleSignOut = () => {
    signOutUser().then(res => {
      if (res.message) {
        toast({
          title: "Success ☺️",
          description: "Sad to see you leave. See you soon!",
          status: "success",
          duration: 9000,
          isClosable: true,
        });
        navigate("/login")
      }
    })
  }
  

  return (
    <div>
        <TopNav />

        <Box display={'flex'} justifyContent={'space-around'} gap={'4'} alignItems={'flex-start'} h={'55vh'} boxShadow={'lg'} w={'60%'} marginX={'auto'} marginY={'20'} p={'6'}>
            <Image w={'40%'} src={Avatar} alt={'avatar'} />
          <Box  w={'50%'}>

          <Text fontSize={'4xl'} fontWeight={'black'}> 👋 Hello There!!</Text>

          <Text fontSize={'5xl'} fontWeight={'black'} marginY={'4'}>I'm {firstAidUser.first_name} {firstAidUser.last_name}</Text>


          <Flex gap={'4'} marginY={'8'}>
            <Flex direction={'column'} gap={'4'}>
              <Text fontWeight={'bold'}>First Name:</Text>
              <Text fontWeight={'bold'}>Last Name:</Text>
              <Text fontWeight={'bold'}>Email:</Text>
            </Flex>

            <Flex direction={'column'} gap={'4'}>
              <Box>{firstAidUser.first_name}</Box>
              <Box>{firstAidUser.last_name}</Box>
              <Box>{firstAidUser.email}</Box>
            </Flex>
          </Flex>

          <Button w={'full'} onClick={handleSignOut} bg={'#D78521'} color={'white'}>Log Out</Button>
          </Box>
        </Box>
    </div>
  )
}

export default Profile