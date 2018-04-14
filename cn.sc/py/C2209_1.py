from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C2209_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_156",          # 01, 1
        "Function_2_168",          # 02, 2
        "Function_3_17A",          # 03, 3
        "Function_4_184",          # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_72(0x4, 0x4)
    OP_71(0x2, 0x20)
    OP_71(0x4, 0x20)
    OP_71(0x2, 0x8)
    OP_71(0x4, 0x8)
    OP_6D(3340, 13200, 3070, 0)
    OP_67(0, 10720, -10000, 0)
    OP_6B(4800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_43(0x101, 0x0, 0x1, 0x1)
    OP_43(0x101, 0x1, 0x1, 0x2)
    OP_43(0x101, 0x2, 0x1, 0x3)
    OP_43(0x101, 0x3, 0x1, 0x4)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(4000)
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C2219   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_156(): pass

    label("Function_1_156")

    OP_6D(90, 28750, 5270, 12000)
    Return()

    # Function_1_156 end

    def Function_2_168(): pass

    label("Function_2_168")

    OP_67(0, 7310, -10000, 12000)
    Return()

    # Function_2_168 end

    def Function_3_17A(): pass

    label("Function_3_17A")

    OP_6B(3560, 12000)
    Return()

    # Function_3_17A end

    def Function_4_184(): pass

    label("Function_4_184")

    OP_6C(338000, 12000)
    Return()

    # Function_4_184 end

    SaveToFile()

Try(main)
