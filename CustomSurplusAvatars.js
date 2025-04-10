import React from 'react';
import Avatar from '@mui/material/Avatar';
import AvatarGroup from '@mui/material/AvatarGroup';
import { useTheme } from '@mui/material/styles';

export default function CustomSurplusAvatars({ darkMode }) {
    const theme = useTheme();

    // Define avatar styles based on dark mode
    const avatarStyles = {
        backgroundColor: darkMode ? theme.palette.grey[900] : theme.palette.grey[500],
        border: `2px solid ${darkMode ? theme.palette.grey[900] : theme.palette.grey[500]}`,
    };

    return (
        <AvatarGroup
            renderSurplus={(surplus) => <span>+{surplus.toString()[0]}k</span>}
            total={4251}
        >
            <Avatar alt="Rakesh" src="/static/images/avatar/1.jpg" sx={avatarStyles} />
            <Avatar alt="Farmer B" src="/static/images/avatar/2.jpg" sx={avatarStyles} />
            <Avatar alt="Farmer C" src="/static/images/avatar/4.jpg" sx={avatarStyles} />
            <Avatar alt="Farmer D" src="/static/images/avatar/5.jpg" sx={avatarStyles} />
        </AvatarGroup>
    );
}
