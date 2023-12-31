# :triangular_flag_on_post: SHIFT (Shared Hosting IP Finder Tool)

:date:**20-06-2023** :pushpin:**Initial Version 1.0.0** :computer:<a href="https://github.com/n4j1Br4ch1D" target="_blank" title="NajibRachid: Agile full-stack developer">NajibRachid</a> :purple_circle:<a href="https://anmoonweb.com/?ref=shift" target="_blank" title="ANMOON: Right talents at the right place ">ANMOON</a>

SHIFT is a penetration testing tool designed to help you identify the IP addresses of shared hosting associated with a specific domain. It checks each IP address  to determine if the domain is hosted on that IP.

<div style="display:flex">
<img src="https://raw.githubusercontent.com/n4j1Br4ch1D/SHIFT/main/assets/SHIFT.png" alt="SHIFT (Shared Hosting IP Finder Tool)" height="300" width="400">
</div>

## Motivation
The development of SHIFT was motivated by the need to automate and streamline the process of bypassing reverse proxies like Cloudflare. In shared hosting environments, multiple domains and subdomains often share the same IP address, presenting a significant challenge for penetration testers and security analysts seeking to identify the precise IP addresses associated with specific domains.

Manually determining the correct IP address for a domain hosted on shared hosting platforms can be a laborious and error-prone task. It typically involves time-consuming manual checks, leading to delays in conducting security assessments and penetration testing activities.

## Features

- [x] Checks range of IP addresses.
- [ ] Set timeout paramter.
- [ ] Add request headers parameter.
- [ ] Show response headers.
- [ ] Check list of IP addresses.
- [ ] Check for a list of domain names.
- [ ] Import list of IP addresses from .txt file.
- [ ] Import list of  domain names From .txt file.
- [ ] Customize check criteria.

## Install
```sh
pip install shift-ip 

```

## Usage
**Syntax**
```sh
shift-ip IP DOMAIN
```

-  Check IP addresses range: between `1` and `24`.
```sh
shift-ip 127.0.0.1/24 example.com
```
**Request headers**

- `Host` header is automatically added. In HTTP it specifies the target server's domain or host name, enabling clients to access specific domains or subdomains hosted on servers with multiple websites.

**Check criteria**

- `Namecheap` shared hosting: valid IP has redirect status response code `301`. 

## Releases

```txt
  - Initial Version 1.0.0 : 20/06/2023
    - Project Setup.
    - Theory & prove of concept.
  - [Agenda] Alpha Version 1.x.x : xx/xx/2023
    - Add timeout paramter.
    - Print found IP at the end.
```

### Contributions

Contributions to SHIFT are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the official GitHub repository: [https://github.com/n4j1Br4ch1D/SHIFT](https://github.com/n4j1Br4ch1D/SHIFT)

### License

SHIFT is open-source and released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute it as per the license terms.
