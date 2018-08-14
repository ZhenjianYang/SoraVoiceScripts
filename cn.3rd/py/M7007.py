from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7007   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7007.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
        '埃尔赛尤',                             # 9
        '',                                     # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_106",          # 01, 1
        "Function_2_13B",          # 02, 2
        "Function_3_89F",          # 03, 3
        "Function_4_D62",          # 04, 4
        "Function_5_E02",          # 05, 5
        "Function_6_1083",         # 06, 6
        "Function_7_12DF",         # 07, 7
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_E9")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_105")

    label("loc_E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_105")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_105")

    Return()

    # Function_0_CA end

    def Function_1_106(): pass

    label("Function_1_106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_END)), "loc_113")
    OP_71(0x409, 0x0)
    ExitThread()

    label("loc_113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124")
    OP_82(0x8F, 0x0)
    OP_82(0x90, 0x0)
    OP_82(0x92, 0x0)

    label("loc_124")

    OP_82(0x93, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_137")
    OP_82(0x94, 0x0)
    Jump("loc_13A")

    label("loc_137")

    OP_82(0x95, 0x0)

    label("loc_13A")

    Return()

    # Function_1_106 end

    def Function_2_13B(): pass

    label("Function_2_13B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-11520, -21000, 16780, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(6280, 0)
    OP_6C(314000, 0)
    OP_6E(477, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-18620, -21500, -27800, 0)
    OP_67(0, 10320, -10000, 0)
    OP_6B(5250, 0)
    OP_6C(315000, 0)
    OP_6E(429, 0)
    OP_82(0x93, 0x0)
    OP_82(0x94, 0x0)
    OP_82(0x95, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xD7, 0x0, 0x64)
    Fade(2000)
    OP_E5(0x0, 0x8, 0x0, 262144)
    OP_E5(0x0, 0x8, 0x1, 262144)
    OP_E5(0x0, 0x8, 0x2, 262144)
    OP_E5(0x0, 0x8, 0x3, 262144)
    OP_E5(0x0, 0x8, 0x4, 262144)
    OP_E5(0x0, 0x8, 0x5, 262144)
    OP_E5(0x0, 0x8, 0x6, 262144)
    OP_E5(0x0, 0x8, 0x7, 262144)
    OP_E5(0x0, 0x8, 0x8, 262144)
    OP_E5(0x0, 0x8, 0x9, 262144)
    OP_E5(0x0, 0x8, 0xA, 262144)
    OP_E5(0x0, 0x8, 0xB, 262144)
    OP_E5(0x0, 0x8, 0xC, 262144)
    OP_E5(0x0, 0x8, 0xD, 262144)
    OP_E5(0x0, 0x8, 0xE, 262144)
    OP_E5(0x0, 0x8, 0xF, 262144)
    OP_E5(0x0, 0x8, 0x10, 262144)
    OP_E5(0x0, 0x8, 0x11, 262144)
    OP_E5(0x0, 0x8, 0x12, 262144)
    OP_E5(0x0, 0x8, 0x13, 262144)
    OP_E5(0x0, 0x8, 0x14, 262144)
    OP_E5(0x0, 0x8, 0x15, 262144)
    OP_E5(0x0, 0x8, 0x16, 262144)
    OP_E5(0x0, 0x8, 0x17, 262144)
    OP_E5(0x0, 0x8, 0x18, 262144)
    OP_E5(0x0, 0x8, 0x19, 262144)
    OP_E5(0x0, 0x8, 0x1A, 262144)
    OP_E5(0x0, 0x8, 0x1B, 262144)
    OP_E5(0x0, 0x8, 0x1C, 262144)
    OP_E5(0x0, 0x8, 0x1D, 262144)
    OP_E5(0x0, 0x8, 0x1E, 262144)
    OP_E5(0x0, 0x8, 0x1F, 262144)
    OP_E5(0x0, 0x8, 0x20, 262144)
    OP_E5(0x0, 0x8, 0x21, 262144)
    OP_E5(0x0, 0x8, 0x22, 262144)
    OP_E5(0x0, 0x8, 0x23, 262144)
    OP_E5(0x0, 0x8, 0x24, 262144)
    OP_E5(0x0, 0x8, 0x25, 262144)
    OP_E5(0x0, 0x8, 0x26, 262144)
    OP_E5(0x0, 0x8, 0x27, 262144)
    OP_E5(0x0, 0x8, 0x28, 262144)
    OP_E5(0x0, 0x8, 0x29, 262144)
    OP_E5(0x0, 0x8, 0x2A, 262144)
    OP_E5(0x0, 0x8, 0x2B, 262144)
    OP_E5(0x0, 0x8, 0x2C, 262144)
    OP_E5(0x0, 0x8, 0x2D, 262144)
    OP_E5(0x0, 0x8, 0x2E, 262144)
    OP_E5(0x0, 0x8, 0x2F, 262144)
    OP_E5(0x0, 0x8, 0x30, 262144)
    OP_E5(0x0, 0x8, 0x31, 262144)
    OP_E5(0x0, 0x8, 0x32, 262144)
    OP_E5(0x0, 0x8, 0x33, 262144)
    OP_E5(0x0, 0x8, 0x34, 262144)
    OP_E5(0x0, 0x8, 0x35, 262144)
    OP_E5(0x0, 0x8, 0x36, 262144)
    OP_E5(0x0, 0x8, 0x37, 262144)
    OP_E5(0x0, 0x8, 0x38, 262144)
    OP_E5(0x0, 0x8, 0x39, 262144)
    OP_E5(0x0, 0x8, 0x3A, 262144)
    OP_E5(0x0, 0x8, 0x3B, 262144)
    OP_E5(0x0, 0x8, 0x3C, 262144)
    OP_E5(0x0, 0x8, 0x3D, 262144)
    OP_E5(0x0, 0x8, 0x3E, 262144)
    OP_E5(0x0, 0x8, 0x3F, 262144)
    OP_E5(0x0, 0x8, 0x40, 262144)
    OP_E5(0x0, 0x8, 0x41, 262144)
    OP_E5(0x0, 0x8, 0x42, 262144)
    OP_E5(0x0, 0x8, 0x43, 262144)
    OP_E5(0x0, 0x8, 0x44, 262144)
    OP_E5(0x0, 0x8, 0x45, 262144)
    OP_E5(0x0, 0x8, 0x46, 262144)
    OP_E5(0x0, 0x8, 0x47, 262144)
    OP_E5(0x0, 0x8, 0x48, 262144)
    OP_E5(0x0, 0x8, 0x49, 262144)
    OP_E5(0x0, 0x8, 0x4A, 262144)
    OP_E5(0x0, 0x8, 0x4B, 262144)
    OP_E5(0x0, 0x8, 0x4C, 262144)
    OP_E5(0x0, 0x8, 0x4D, 262144)
    OP_E5(0x0, 0x8, 0x4E, 262144)
    OP_E5(0x0, 0x8, 0x4F, 262144)
    OP_E5(0x0, 0x8, 0x50, 262144)
    OP_E5(0x0, 0x8, 0x51, 262144)
    OP_E5(0x0, 0x8, 0x52, 262144)
    OP_E5(0x0, 0x8, 0x53, 262144)
    OP_E5(0x0, 0x8, 0x54, 262144)
    OP_E5(0x0, 0x8, 0x55, 262144)
    OP_E5(0x0, 0x8, 0x56, 262144)
    OP_E5(0x0, 0x8, 0x57, 262144)
    OP_E5(0x0, 0x8, 0x58, 262144)
    OP_E5(0x0, 0x8, 0x59, 262144)
    OP_E5(0x0, 0x8, 0x5A, 262144)
    OP_E5(0x0, 0x8, 0x5B, 262144)
    OP_E5(0x0, 0x8, 0x5C, 262144)
    OP_E5(0x0, 0x8, 0x5D, 262144)
    OP_E5(0x2, 0x8, 0x0, 700)
    OP_E5(0x2, 0x8, 0x1, 700)
    OP_E5(0x2, 0x8, 0x2, 700)
    OP_E5(0x2, 0x8, 0x3, 700)
    OP_E5(0x2, 0x8, 0x4, 700)
    OP_E5(0x2, 0x8, 0x5, 700)
    OP_E5(0x2, 0x8, 0x6, 700)
    OP_E5(0x2, 0x8, 0x7, 700)
    OP_E5(0x2, 0x8, 0x8, 700)
    OP_E5(0x2, 0x8, 0x9, 700)
    OP_E5(0x2, 0x8, 0xA, 700)
    OP_E5(0x2, 0x8, 0xB, 700)
    OP_E5(0x2, 0x8, 0xC, 700)
    OP_E5(0x2, 0x8, 0xD, 700)
    OP_E5(0x2, 0x8, 0xE, 700)
    OP_E5(0x2, 0x8, 0xF, 700)
    OP_E5(0x2, 0x8, 0x10, 700)
    OP_E5(0x2, 0x8, 0x11, 700)
    OP_E5(0x2, 0x8, 0x12, 700)
    OP_E5(0x2, 0x8, 0x13, 700)
    OP_E5(0x2, 0x8, 0x14, 700)
    OP_E5(0x2, 0x8, 0x15, 700)
    OP_E5(0x2, 0x8, 0x16, 700)
    OP_E5(0x2, 0x8, 0x17, 700)
    OP_E5(0x2, 0x8, 0x18, 700)
    OP_E5(0x2, 0x8, 0x19, 700)
    OP_E5(0x2, 0x8, 0x1A, 700)
    OP_E5(0x2, 0x8, 0x1B, 700)
    OP_E5(0x2, 0x8, 0x1C, 700)
    OP_E5(0x2, 0x8, 0x1D, 700)
    OP_E5(0x2, 0x8, 0x1E, 700)
    OP_E5(0x2, 0x8, 0x1F, 700)
    OP_E5(0x2, 0x8, 0x20, 700)
    OP_E5(0x2, 0x8, 0x21, 700)
    OP_E5(0x2, 0x8, 0x22, 700)
    OP_E5(0x2, 0x8, 0x23, 700)
    OP_E5(0x2, 0x8, 0x24, 700)
    OP_E5(0x2, 0x8, 0x25, 700)
    OP_E5(0x2, 0x8, 0x26, 700)
    OP_E5(0x2, 0x8, 0x27, 700)
    OP_E5(0x2, 0x8, 0x28, 700)
    OP_E5(0x2, 0x8, 0x29, 700)
    OP_E5(0x2, 0x8, 0x2A, 700)
    OP_E5(0x2, 0x8, 0x2B, 700)
    OP_E5(0x2, 0x8, 0x2C, 700)
    OP_E5(0x2, 0x8, 0x2D, 700)
    OP_E5(0x2, 0x8, 0x2E, 700)
    OP_E5(0x2, 0x8, 0x2F, 700)
    OP_E5(0x2, 0x8, 0x30, 700)
    OP_E5(0x2, 0x8, 0x31, 700)
    OP_E5(0x2, 0x8, 0x32, 700)
    OP_E5(0x2, 0x8, 0x33, 700)
    OP_E5(0x2, 0x8, 0x34, 700)
    OP_E5(0x2, 0x8, 0x35, 700)
    OP_E5(0x2, 0x8, 0x36, 700)
    OP_E5(0x2, 0x8, 0x37, 700)
    OP_E5(0x2, 0x8, 0x38, 700)
    OP_E5(0x2, 0x8, 0x39, 700)
    OP_E5(0x2, 0x8, 0x3A, 700)
    OP_E5(0x2, 0x8, 0x3B, 700)
    OP_E5(0x2, 0x8, 0x3C, 700)
    OP_E5(0x2, 0x8, 0x3D, 700)
    OP_E5(0x2, 0x8, 0x3E, 700)
    OP_E5(0x2, 0x8, 0x3F, 700)
    OP_E5(0x2, 0x8, 0x40, 700)
    OP_E5(0x2, 0x8, 0x41, 700)
    OP_E5(0x2, 0x8, 0x42, 700)
    OP_E5(0x2, 0x8, 0x43, 700)
    OP_E5(0x2, 0x8, 0x44, 700)
    OP_E5(0x2, 0x8, 0x45, 700)
    OP_E5(0x2, 0x8, 0x46, 700)
    OP_E5(0x2, 0x8, 0x47, 700)
    OP_E5(0x2, 0x8, 0x48, 700)
    OP_E5(0x2, 0x8, 0x49, 700)
    OP_E5(0x2, 0x8, 0x4A, 700)
    OP_E5(0x2, 0x8, 0x4B, 700)
    OP_E5(0x2, 0x8, 0x4C, 700)
    OP_E5(0x2, 0x8, 0x4D, 700)
    OP_E5(0x2, 0x8, 0x4E, 700)
    OP_E5(0x2, 0x8, 0x4F, 700)
    OP_E5(0x2, 0x8, 0x50, 700)
    OP_E5(0x2, 0x8, 0x51, 700)
    OP_E5(0x2, 0x8, 0x52, 700)
    OP_E5(0x2, 0x8, 0x53, 700)
    OP_E5(0x2, 0x8, 0x54, 700)
    OP_E5(0x2, 0x8, 0x55, 700)
    OP_E5(0x2, 0x8, 0x56, 700)
    OP_E5(0x2, 0x8, 0x57, 700)
    OP_E5(0x2, 0x8, 0x58, 700)
    OP_E5(0x2, 0x8, 0x59, 700)
    OP_E5(0x2, 0x8, 0x5A, 700)
    OP_E5(0x2, 0x8, 0x5B, 700)
    OP_E5(0x2, 0x8, 0x5C, 700)
    OP_E5(0x2, 0x8, 0x5D, 700)
    OP_0D()
    Sleep(1000)

    def lambda_7DE():
        OP_6D(-19420, -21050, -28140, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_7DE)

    def lambda_7F6():
        OP_67(0, 5720, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7F6)

    def lambda_80E():
        OP_6B(6840, 10000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_80E)

    def lambda_81E():
        OP_6C(335000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_81E)

    def lambda_82E():
        OP_6E(484, 10000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_82E)
    OP_22(0x77, 0x1, 0x64)
    OP_22(0x125, 0x1, 0x3C)
    OP_B0(0x8, 0x1E)
    OP_6F(0x8, 1)
    OP_70(0x8, 0x8C)
    OP_73(0x8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 140)
    OP_70(0x8, 0x96)
    OP_22(0x125, 0x1, 0x50)
    Sleep(3000)
    WaitChrThread(0xEE, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x2)
    OP_44(0xEF, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_13B end

    def Function_3_89F(): pass

    label("Function_3_89F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "scraft\\sc000_33.eff")
    LoadEffect(0x1, "map\\mp205_00.eff")
    LoadEffect(0x2, "map\\mp201_01.eff")
    OP_6D(-11520, -21000, 16780, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(6280, 0)
    OP_6C(314000, 0)
    OP_6E(477, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-19470, -22500, -27530, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(315000, 0)
    OP_6E(530, 0)
    OP_A1(0x10, 0x8)
    SetChrPos(0x10, -26000, -23000, -28700, 90)
    OP_22(0x125, 0x0, 0x64)
    OP_B0(0x8, 0x3C)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 140)
    OP_70(0x8, 0x96)
    OP_82(0x93, 0x0)
    OP_82(0x94, 0x0)
    OP_82(0x95, 0x0)
    ClearMapFlags(0x10)

    def lambda_9BC():
        OP_6E(600, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9BC)

    def lambda_9CC():
        OP_67(0, 2800, -10000, 10000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9CC)
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x2008, 0x0)
    ExitThread()
    OP_73(0x8)
    OP_6F(0x8, 150)
    OP_70(0x8, 0x14A)
    Sleep(1500)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(300)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(300)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(300)
    OP_73(0x8)
    OP_71(0x2008, 0x0)
    ExitThread()
    OP_6F(0x8, 330)
    OP_70(0x8, 0x1AE)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0x4)

    def lambda_A4B():
        OP_6D(-19470, -22500, -28530, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_A4B)
    Sleep(2000)
    Fade(1000)
    OP_44(0xEF, 0x1)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x1)
    OP_44(0xEE, 0x3)
    OP_6D(-30270, 6000, -42290, 0)
    OP_67(0, 7550, -10000, 0)
    OP_6B(7990, 0)
    OP_6C(44000, 0)
    OP_6E(579, 0)

    def lambda_ABA():
        OP_6D(-30360, 6000, -59070, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_ABA)
    Sleep(5000)
    Fade(1000)
    OP_44(0xEE, 0x0)
    OP_6D(-18640, -20300, -44520, 0)
    OP_67(0, 9690, -10000, 0)
    OP_6B(5670, 0)
    OP_6C(212000, 0)
    OP_6E(498, 0)

    def lambda_B1D():
        OP_6B(7630, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_B1D)
    WaitChrThread(0x10, 0x0)
    OP_22(0x159, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_44(0xEE, 0x0)
    OP_6D(-46080, -35750, -103180, 0)
    OP_67(0, 3680, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(249000, 0)
    OP_6E(650, 0)
    PlayEffect(0x1, 0x0, 0xFF, -40680, -35000, -700010, 180, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_BBB():

        label("loc_BBB")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_BBB")

    QueueWorkItem2(0xEF, 3, lambda_BBB)
    SetChrPos(0x10, -20680, -23000, -20010, 180)

    def lambda_BE7():
        OP_6D(-53480, -45650, -120930, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_BE7)

    def lambda_BFF():
        OP_67(0, 4200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_BFF)

    def lambda_C17():
        OP_6B(9410, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_C17)

    def lambda_C27():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_C27)

    def lambda_C37():
        OP_6E(898, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C37)
    PlayEffect(0x2, 0xFF, 0x10, 0, 1500, 16000, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x10, 7300, -1600, 12000, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x10, -7300, -1600, 12000, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x5)
    Sleep(1500)
    Sleep(1000)
    OP_82(0x80, 0x2)

    def lambda_CFF():
        OP_6D(-52000, -30000, -180740, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_CFF)

    def lambda_D17():
        OP_67(0, -2000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_D17)

    def lambda_D2F():
        OP_6C(220000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_D2F)
    Sleep(1000)
    OP_43(0xF1, 0x0, 0x0, 0x7)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_89F end

    def Function_4_D62(): pass

    label("Function_4_D62")


    def lambda_D68():
        OP_8F(0xFE, 0xFFFF9A70, 0xFFFFA628, 0xFFFF8044, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D68)
    WaitChrThread(0xFE, 0x1)

    def lambda_D88():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFFF502E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D88)

    def lambda_DA3():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DA3)
    Sleep(500)

    def lambda_DB6():
        OP_8C(0xFE, 180, 15)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DB6)
    Sleep(500)

    def lambda_DC9():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC9)
    Sleep(2000)

    def lambda_DDC():
        OP_8C(0xFE, 180, 15)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DDC)
    Sleep(500)

    def lambda_DEF():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DEF)
    WaitChrThread(0xFE, 0x2)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_D62 end

    def Function_5_E02(): pass

    label("Function_5_E02")


    def lambda_E08():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E08)
    Sleep(100)

    def lambda_E28():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E28)
    Sleep(100)

    def lambda_E48():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E48)
    Sleep(100)

    def lambda_E68():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E68)
    Sleep(100)

    def lambda_E88():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E88)
    Sleep(100)

    def lambda_EA8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA8)
    Sleep(100)

    def lambda_EC8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EC8)
    Sleep(100)

    def lambda_EE8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE8)
    Sleep(100)

    def lambda_F08():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F08)
    Sleep(100)

    def lambda_F28():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x6978, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F28)
    Sleep(100)

    def lambda_F48():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F48)
    Sleep(100)

    def lambda_F68():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F68)
    Sleep(100)

    def lambda_F88():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F88)
    Sleep(100)

    def lambda_FA8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA8)
    Sleep(100)

    def lambda_FC8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC8)
    Sleep(100)

    def lambda_FE8():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FE8)
    Sleep(100)

    def lambda_1008():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1008)
    Sleep(100)

    def lambda_1028():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1028)
    Sleep(100)

    def lambda_1048():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1048)
    Sleep(100)

    def lambda_1068():
        OP_8F(0xFE, 0xFFFC05B8, 0xFFFE7960, 0xFF9CD156, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1068)
    Sleep(100)
    Return()

    # Function_5_E02 end

    def Function_6_1083(): pass

    label("Function_6_1083")


    def lambda_1089():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1089)
    Sleep(100)

    def lambda_10A9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A9)
    Sleep(100)

    def lambda_10C9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C9)
    Sleep(100)

    def lambda_10E9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E9)
    Sleep(100)

    def lambda_1109():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1109)
    Sleep(100)

    def lambda_1129():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1129)
    Sleep(100)

    def lambda_1149():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1149)
    Sleep(100)

    def lambda_1169():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1169)
    Sleep(100)

    def lambda_1189():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1189)
    Sleep(100)

    def lambda_11A9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x6978, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A9)
    Sleep(100)

    def lambda_11C9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11C9)
    Sleep(100)

    def lambda_11E9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E9)
    Sleep(100)

    def lambda_1209():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1209)
    Sleep(100)

    def lambda_1229():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1229)
    Sleep(100)

    def lambda_1249():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1249)
    Sleep(100)

    def lambda_1269():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x11170, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1269)
    Sleep(100)

    def lambda_1289():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1289)
    Sleep(100)

    def lambda_12A9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12A9)
    Sleep(100)

    def lambda_12C9():
        OP_8F(0xFE, 0xFFFFB708, 0xFFFFA628, 0xFFCA9816, 0x186A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12C9)
    Return()

    # Function_6_1083 end

    def Function_7_12DF(): pass

    label("Function_7_12DF")

    OP_24(0x125, 0x5A)
    OP_24(0x159, 0x5A)
    Sleep(300)
    OP_24(0x125, 0x50)
    OP_24(0x159, 0x50)
    Sleep(300)
    OP_24(0x125, 0x46)
    OP_24(0x159, 0x46)
    Sleep(300)
    OP_24(0x125, 0x3C)
    OP_24(0x159, 0x3C)
    Sleep(300)
    OP_24(0x125, 0x32)
    OP_24(0x159, 0x32)
    Sleep(300)
    OP_24(0x125, 0x28)
    OP_24(0x159, 0x28)
    Sleep(300)
    OP_24(0x125, 0x1E)
    OP_24(0x159, 0x1E)
    Sleep(300)
    OP_24(0x125, 0x14)
    OP_24(0x159, 0x14)
    Sleep(300)
    OP_24(0x125, 0xA)
    OP_24(0x159, 0xA)
    Sleep(300)
    OP_24(0x125, 0x0)
    OP_24(0x159, 0x0)
    OP_23(0x125)
    OP_23(0x159)
    Return()

    # Function_7_12DF end

    SaveToFile()

Try(main)
