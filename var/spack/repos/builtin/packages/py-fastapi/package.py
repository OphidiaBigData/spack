# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyFastapi(PythonPackage):
    """FastAPI framework, high performance, easy to learn, fast to code, ready for production"""

    homepage = "https://github.com/tiangolo/fastapi"
    pypi = "fastapi/fastapi-0.88.0.tar.gz"

    version("0.88.0", sha256="915bf304180a0e7c5605ec81097b7d4cd8826ff87a02bb198e336fb9f3b5ff02")

    variant("all", default=False, description="Build all optional dependencies")

    depends_on("py-hatchling", type="build")
    depends_on("py-starlette@0.22.0", type=("build", "run"))
    depends_on("py-pydantic@1.6.2:1.6,1.7.4:1.7,1.8.2:1", type=("build", "run"))

    with when("+all"):
        depends_on("py-httpx@0.23:", type=("build", "run"))
        depends_on("py-jinja2@2.11.2:", type=("build", "run"))
        depends_on("py-python-multipart@0.0.5:", type=("build", "run"))
        depends_on("py-itsdangerous@1.1:", type=("build", "run"))
        depends_on("py-pyyaml@5.3.1:", type=("build", "run"))
        depends_on("py-ujson@4.0.1:", type=("build", "run"))
        depends_on("py-orjson@3.2.1:", type=("build", "run"))
        depends_on("py-email-validator@1.1.1:", type=("build", "run"))
        depends_on("py-uvicorn@0.12:+standard", type=("build", "run"))

        conflicts("^py-ujson@4.0.2,4.1.0,4.2.0,4.3.0,5.0.0,5.1.0")
