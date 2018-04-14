from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5414   ._SN',
        MapName             = 'other',
        Location            = 'C5414.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '剑帝莱维',                             # 9
        '结社艇',                               # 10
        '结社艇',                               # 11
        '结社艇',                               # 12
        '结社艇',                               # 13
        '结社艇',                               # 14
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


    AddCharChip(
        'ED6_DT07/CH02040 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02040P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_19B",          # 01, 1
        "Function_2_1BF",          # 02, 2
        "Function_3_32E",          # 03, 3
        "Function_4_5B9",          # 04, 4
        "Function_5_5FC",          # 05, 5
        "Function_6_68A",          # 06, 6
        "Function_7_718",          # 07, 7
        "Function_8_7A6",          # 08, 8
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_183")
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_19A")

    label("loc_183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_19A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 3)

    label("loc_19A")

    Return()

    # Function_0_172 end

    def Function_1_19B(): pass

    label("Function_1_19B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B9")

    OP_22(0x1C3, 0x1, 0x64)
    Return()

    # Function_1_19B end

    def Function_2_1BF(): pass

    label("Function_2_1BF")

    EventBegin(0x0)
    OP_6D(4910, -1800, 22110, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(225000, 0)
    OP_6E(305, 0)
    SetChrPos(0x101, 5990, -1800, 23310, 90)
    OP_22(0x131, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_224():
        OP_6D(4910, -1800, 22110, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_224)

    def lambda_23C():
        OP_67(0, 3270, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23C)

    def lambda_254():
        OP_6B(4420, 12000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_254)

    def lambda_264():
        OP_6C(213000, 12000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_264)

    def lambda_274():
        OP_6E(1434, 12000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_274)
    Sleep(10000)
    FadeToDark(2000, 0, -1)
    OP_24(0x131, 0x46)
    Sleep(300)
    OP_24(0x131, 0x3C)
    Sleep(300)
    OP_24(0x131, 0x32)
    Sleep(300)
    OP_24(0x131, 0x28)
    Sleep(300)
    OP_24(0x131, 0x1E)
    Sleep(300)
    OP_24(0x131, 0x14)
    Sleep(300)
    OP_23(0x131)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    PlayMovie(0x0, "ED6_DT40.dat", 0x0, 0x1)

    label("loc_2EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_304")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_301")
    Jump("loc_304")

    label("loc_301")

    Jump("loc_2EA")

    label("loc_304")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BF end

    def Function_3_32E(): pass

    label("Function_3_32E")

    EventBegin(0x0)
    OP_11(0xFF, 0xFF, 0xFF, 0xF424, 0x493E0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 5990, -1800, 24620, 90)
    SetChrPos(0x101, 5990, -1800, 23310, 90)
    OP_6D(5990, -1800, 23310, 0)
    OP_67(0, 3220, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(251000, 0)
    OP_6E(1188, 0)
    OP_22(0x131, 0x1, 0x46)
    OP_A1(0x9, 0x2)
    OP_A1(0xA, 0x3)
    OP_A1(0xB, 0x4)
    OP_A1(0xC, 0x5)
    OP_A1(0xD, 0x6)
    OP_71(0x2, 0x2)
    OP_71(0x2, 0x20)
    OP_72(0x2, 0x4)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x3, 0x2)
    OP_71(0x3, 0x20)
    OP_72(0x3, 0x4)
    OP_6F(0x3, 800)
    OP_70(0x3, 0x384)
    OP_71(0x4, 0x2)
    OP_71(0x4, 0x20)
    OP_72(0x4, 0x4)
    OP_6F(0x4, 800)
    OP_70(0x4, 0x384)
    OP_71(0x5, 0x2)
    OP_71(0x5, 0x20)
    OP_72(0x5, 0x4)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_71(0x6, 0x2)
    OP_71(0x6, 0x20)
    OP_72(0x6, 0x4)
    OP_6F(0x6, 800)
    OP_70(0x6, 0x384)
    SetChrPos(0x9, 26000, 3000, 280000, 0)
    SetChrPos(0xA, 48000, 2000, 280000, 0)
    SetChrPos(0xB, 68000, 4000, 280000, 0)
    SetChrPos(0xC, 88000, 2000, 280000, 0)
    SetChrPos(0xD, 108000, 4000, 280000, 0)
    OP_D1(9, 0, 180000, 0, 0)
    OP_D1(10, 0, 180000, 0, 0)
    OP_D1(11, 0, 180000, 0, 0)
    OP_D1(12, 0, 180000, 0, 0)
    OP_D1(13, 0, 180000, 0, 0)
    FadeToDark(0, 0, -1)
    OP_43(0x9, 0x0, 0x0, 0x4)
    OP_43(0xA, 0x0, 0x0, 0x5)
    OP_43(0xB, 0x0, 0x0, 0x6)
    OP_43(0xC, 0x0, 0x0, 0x7)
    OP_43(0xD, 0x0, 0x0, 0x8)
    Sleep(2000)
    OP_22(0x79, 0x1, 0x3C)
    Sleep(1000)
    OP_22(0x79, 0x1, 0x46)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_22(0x79, 0x1, 0x50)
    Sleep(1000)
    OP_22(0x79, 0x1, 0x5A)
    Sleep(1000)

    def lambda_570():
        OP_6D(59460, -1800, 5100, 6000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_570)

    def lambda_588():
        OP_6C(228000, 6000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_588)
    WaitChrThread(0x0, 0x0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_3_32E end

    def Function_4_5B9(): pass

    label("Function_4_5B9")


    def lambda_5BF():
        OP_D1(254, 0, 180000, 25000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5BF)
    OP_8F(0xFE, 0x6590, 0xBB8, 0xFFFFB1E0, 0x9C40, 0x0)
    OP_8F(0xFE, 0xEA60, 0x1770, 0xFFFB6C20, 0x9C40, 0x0)
    Return()

    # Function_4_5B9 end

    def Function_5_5FC(): pass

    label("Function_5_5FC")

    Sleep(1000)

    def lambda_607():
        OP_D1(254, 0, 175000, 30000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_607)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x7530, 0xBB8, 0xFFFFB1E0)
    OP_98(0x1, 0x15F90, 0xFFFFF060, 0xFFFB6C20)

    def lambda_641():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_641)
    Sleep(2000)

    def lambda_656():
        OP_D1(254, 0, 175000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_656)
    WaitChrThread(0xFE, 0x3)

    def lambda_675():
        OP_D1(254, 0, 175000, 15000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_675)
    Return()

    # Function_5_5FC end

    def Function_6_68A(): pass

    label("Function_6_68A")

    Sleep(2000)

    def lambda_695():
        OP_D1(254, 0, 180000, 35000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_695)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x7530, 0x3E8, 0xFFFFB1E0)
    OP_98(0x1, 0x1D4C0, 0xFFFFC950, 0xFFFB6C20)

    def lambda_6CF():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CF)
    Sleep(2000)

    def lambda_6E4():
        OP_D1(254, 0, 170000, 35000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6E4)
    WaitChrThread(0xFE, 0x3)

    def lambda_703():
        OP_D1(254, 0, 170000, 15000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_703)
    Return()

    # Function_6_68A end

    def Function_7_718(): pass

    label("Function_7_718")

    Sleep(3000)

    def lambda_723():
        OP_D1(254, 0, 180000, 40000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_723)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x7530, 0xFFFFFC18, 0xFFFFB1E0)
    OP_98(0x1, 0x249F0, 0xFFFFA240, 0xFFFB6C20)

    def lambda_75D():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75D)
    Sleep(2000)

    def lambda_772():
        OP_D1(254, 0, 165000, 40000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_772)
    WaitChrThread(0xFE, 0x3)

    def lambda_791():
        OP_D1(254, 0, 165000, 15000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_791)
    Return()

    # Function_7_718 end

    def Function_8_7A6(): pass

    label("Function_8_7A6")

    Sleep(4000)

    def lambda_7B1():
        OP_D1(254, 0, 180000, 45000, 8000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7B1)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x7530, 0xFFFFF448, 0xFFFFB1E0)
    OP_98(0x1, 0x2BF20, 0xFFFF7B30, 0xFFFB6C20)

    def lambda_7EB():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7EB)
    Sleep(2000)

    def lambda_800():
        OP_D1(254, 0, 160000, 45000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_800)
    WaitChrThread(0xFE, 0x3)

    def lambda_81F():
        OP_D1(254, 0, 160000, 15000, 10000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_81F)
    Return()

    # Function_8_7A6 end

    SaveToFile()

Try(main)
