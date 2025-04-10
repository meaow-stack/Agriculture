import React, { useEffect } from 'react';
import Swal from 'sweetalert2';
import 'animate.css';

const TermsAndConditions = () => {
    useEffect(() => {
        const showTermsAndConditions = async () => {
            const { value: accept } = await Swal.fire({
                title: "Terms and conditions",
                input: "checkbox",
                inputValue: 1,
                inputPlaceholder: "I agree with the terms and conditions",
                confirmButtonText: 'Continue&nbsp;<i class="fa fa-arrow-right"></i>',
                inputValidator: (result) => {
                    return !result && "You need to agree with T&C";
                },
                // Adding animation classes
                showClass: {
                    popup: 'animate__animated animate__fadeInDown'
                },
                hideClass: {
                    popup: 'animate__animated animate__fadeOutUp'
                }
            });

            if (accept) {
                Swal.fire({
                    title: "You agreed with T&C :)",
                    showClass: {
                        popup: 'animate__animated animate__fadeInDown'
                    },
                    hideClass: {
                        popup: 'animate__animated animate__fadeOutUp'
                    }
                });
            }
        };

        showTermsAndConditions();
    }, []);

    return null; // The component doesn't render any UI, just runs the effect
};

export default TermsAndConditions;
