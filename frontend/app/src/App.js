import * as React from 'react';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import axios from 'axios';
import TextField from '@mui/material/TextField';
import config from './config'

export default function App() {

    const [jsonValue, setJsonValue] = React.useState('');
    const [jsonObject, setJsonObject] = React.useState([]);

    const handleSubmitToAPI = async () => {
        console.log(jsonValue);
        try {
            let res = await axios({
                url: config().BASE_BACKEND_URL + 'api/colors/get-colors/',
                method: 'post',
                data: jsonValue,
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            // Don't forget to return something
            res = res.data;
            setJsonObject(res);
            console.log(res);
        } catch (error) {
            console.log('Error');
        }
    };

    return (
        <Grid container spacing={2} style={{
          width: '80%',
          marginLeft: '10%',
          marginTop: '7.5%',
        }}>
            <Grid item xs={6}>
                <Paper elevation={3}>
                    <TextField
                        label="JSON"
                        multiline
                        fullWidth
                        rows={15}
                        variant="standard"
                        onChange={(event) => {
                            setJsonValue(event.target.value);
                        }}
                    />
                </Paper>
            </Grid>
            <Grid item xs={6}>
                <Box
                    sx={{
                        p: 2,
                        bgcolor: 'white',
                        display: 'grid',
                        gap: 0.1
                    }}
                >
                    {jsonValue.length !== 0 && jsonObject.map((color) => (
                    <Paper elevation={1} sx={{
                        bgcolor: color,
                        minHeight: '69px'
                    }}>

                    </Paper>
                    ))}
                </Box>
            </Grid>
            <Grid item xs={2}>
                <Button
                    variant="contained"
                    onClick={handleSubmitToAPI}
                >
                    Send
                </Button>
            </Grid>
        </Grid>
    );
}
