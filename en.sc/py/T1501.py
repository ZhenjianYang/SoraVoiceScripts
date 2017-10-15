from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1501   ._SN',
        MapName             = 'Bose',
        Location            = 'T1501.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'New Ansel Path',                       # 9
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


    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_F4",           # 01, 1
        "Function_2_10C",          # 02, 2
        "Function_3_1D9",          # 03, 3
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_E0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_F3")

    label("loc_E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_F3")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_F3")

    Return()

    # Function_0_CA end

    def Function_1_F4(): pass

    label("Function_1_F4")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x230046)
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_F4 end

    def Function_2_10C(): pass

    label("Function_2_10C")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrPos(0x0, -10100, 0, 50030, 0)
    OP_6D(-10100, 0, 50030, 0)
    OP_67(0, 9320, -10000, 0)
    OP_6B(6520, 0)
    OP_6C(235000, 0)
    OP_6E(315, 0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_178():
        OP_6D(-11250, 0, 47500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_178)

    def lambda_190():
        OP_67(0, 6590, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_190)

    def lambda_1A8():
        OP_6B(5880, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1A8)
    OP_6E(256, 7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_10C end

    def Function_3_1D9(): pass

    label("Function_3_1D9")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrPos(0x0, -10100, 0, 50030, 0)
    OP_6D(-5570, 0, 47640, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(4650, 0)
    OP_6C(142000, 0)
    OP_6E(390, 0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    FadeToBright(1000, 0)

    def lambda_244():
        OP_6D(-3630, 0, 45060, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_244)

    def lambda_25C():
        OP_6B(4400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_25C)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1511   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1D9 end

    SaveToFile()

Try(main)
