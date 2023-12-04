import React, {useState, Fragment} from 'react';
import {FaGithub} from 'react-icons/fa';
function classNames(...classes) {
    return classes.filter(Boolean).join(' ');
  }

const Navbar = () => {
    const [nav, setNav] = useState(false);
    const handleClick = () => setNav(!nav);

    return (
        <div className= 'fixed w-full h-[80px] flex justify-between items-center px-4 bg-[#0e2250] text-white-300'> 
            
            <div>
                 {/* menu */}
                <ul className= 'hidden md:flex'>
                  <li className='p-4 font-bold text-white'>          
                       <a href="/">Home</a>
                </li>
          <li className='p-4 font-bold text-white'>
                         <a href='/About'>About</a>
                         </li>
      </ul>
    </div>
        <div className='hidden lg:flex fixed flex-col top-[35%] left-0'>
            <ul>
                <li className='w-[160px] h-[60px] flex justify-between items-center ml-[-100px] hover:ml-[-10px] duration-300 bg-[#333333]'>
                    <a
                    className='flex justify-between items-center w-full text-gray-300'
                    href='https://github.com/Drewski2222/DSAProject3'
                >
                    Github <FaGithub size={30} />
                    </a>
                </li>               
            </ul>
        </div>
    </div>
    );
};

export default Navbar;

