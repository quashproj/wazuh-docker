{
  description = "Wazuh extensions dev env";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/release-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let

          pkgs = import nixpkgs {
            inherit  system;
            config = {
              allowUnfree = true;
            };
          };
 

        in
        with pkgs;
        {
          devShells.default = mkShell {

            packages = [
              (pkgs.python3.withPackages (pkgs: [
                # select Python packages here
                pkgs.pandas
                pkgs.requests
               ]))
            ];
            shellHook = ''
              echo "Wazuh extensiond dev env"
              echo " - ${pkgs.go.name}"
              echo " - ${pkgs.python3.name}"
            '';
          };
        }
      );
}
