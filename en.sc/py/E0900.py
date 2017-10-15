from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0900   ._SN',
        MapName             = 'Event',
        Location            = 'E0900.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Captain Schwarz',                      # 9
        'General Morgan',                       # 10
        'Nial',                                 # 11
        'Dorothy',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Arseille',                             # 17
        'Patrol Boat',                          # 18
        'Ancient Dragon Ragnard',               # 19
        'Boat',                                 # 20
        '竜',                                   # 21
        'Professor Russell',                    # 22
        'Royal Guardsman',                      # 23
        'Mechanic',                             # 24
        'Mechanic',                             # 25
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
        'ED6_DT27/CH03580 ._CH',             # 00
        'ED6_DT07/CH02080 ._CH',             # 01
        'ED6_DT07/CH02060 ._CH',             # 02
        'ED6_DT07/CH02070 ._CH',             # 03
        'ED6_DT07/CH01300 ._CH',             # 04
        'ED6_DT06/CH20063 ._CH',             # 05
        'ED6_DT06/CH20064 ._CH',             # 06
        'ED6_DT07/CH00324 ._CH',             # 07
        'ED6_DT07/CH02020 ._CH',             # 08
        'ED6_DT07/CH01320 ._CH',             # 09
        'ED6_DT07/CH01450 ._CH',             # 0A
        'ED6_DT07/CH01640 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH03580P._CP',             # 00
        'ED6_DT07/CH02080P._CP',             # 01
        'ED6_DT07/CH02060P._CP',             # 02
        'ED6_DT07/CH02070P._CP',             # 03
        'ED6_DT07/CH01300P._CP',             # 04
        'ED6_DT06/CH20063P._CP',             # 05
        'ED6_DT06/CH20064P._CP',             # 06
        'ED6_DT07/CH00324P._CP',             # 07
        'ED6_DT07/CH02020P._CP',             # 08
        'ED6_DT07/CH01320P._CP',             # 09
        'ED6_DT07/CH01450P._CP',             # 0A
        'ED6_DT07/CH01640P._CP',             # 0B
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1C5,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_38A",          # 01, 1
        "Function_2_399",          # 02, 2
        "Function_3_EB5",          # 03, 3
        "Function_4_ED9",          # 04, 4
        "Function_5_109C",         # 05, 5
        "Function_6_2BE1",         # 06, 6
        "Function_7_2C1E",         # 07, 7
        "Function_8_2C38",         # 08, 8
        "Function_9_2C7E",         # 09, 9
        "Function_10_2CDF",        # 0A, 10
        "Function_11_2D25",        # 0B, 11
        "Function_12_2D6B",        # 0C, 12
        "Function_13_2DB1",        # 0D, 13
        "Function_14_2EB4",        # 0E, 14
        "Function_15_313D",        # 0F, 15
        "Function_16_3313",        # 10, 16
        "Function_17_3392",        # 11, 17
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_340")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_389")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_35F")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_389")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_379")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_389")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_389")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_389")

    Return()

    # Function_0_32A end

    def Function_1_38A(): pass

    label("Function_1_38A")

    OP_B1("E0900_1")
    OP_22(0x1C5, 0x0, 0x64)
    Return()

    # Function_1_38A end

    def Function_2_399(): pass

    label("Function_2_399")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    OP_6D(16050, -2990, 10740, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(109000, 0)
    OP_6E(592, 0)
    OP_A1(0x13, 0x3)
    SetChrPos(0x13, 24950, -3000, 26730, 0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_71(0x0, 0x4)
    OP_72(0x4, 0x4)
    OP_71(0x4, 0x20)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 330)
    OP_70(0x4, 0x1AE)
    OP_6F(0x2, 15)
    OP_48()
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_89(0xC, 24810, -2950, 27690, 0)
    OP_89(0xD, 25230, -2930, 26770, 90)
    OP_89(0xE, 24980, -2950, 25390, 180)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrChipByIndex(0xC, 7)
    SetChrChipByIndex(0xD, 7)
    SetChrChipByIndex(0xE, 7)
    SetChrSubChip(0xC, 3)
    SetChrSubChip(0xD, 3)
    SetChrSubChip(0xE, 3)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    LoadEffect(0x0, "map\\\\mpsibuk.eff")
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    LoadEffect(0x2, "map\\\\mp013_00.eff")
    LoadEffect(0x3, "map\\\\mp013_01.eff")
    OP_A1(0x10, 0x4)
    SetChrPos(0x10, -69820, 15000, 28400, 90)
    ClearChrFlags(0x10, 0x100)
    OP_D1(16, 0, 90000, 0, 0)

    def lambda_540():
        OP_6B(2960, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_540)
    OP_C8(0x200, 0x46, "C_PLAC16._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(2000)

    def lambda_573():
        OP_6D(18530, -2990, 19010, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_573)

    def lambda_58B():
        OP_67(0, 12280, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58B)

    def lambda_5A3():
        OP_6C(122000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5A3)
    Sleep(500)
    OP_43(0x13, 0x0, 0x0, 0x4)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x2BF20), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x125, 0x1, 0x28)
    OP_24(0x125, 0x28)
    Sleep(1000)
    OP_24(0x125, 0x32)
    Sleep(1000)
    OP_24(0x125, 0x3C)
    Sleep(1000)
    OP_24(0x125, 0x46)
    Sleep(1000)
    OP_24(0x125, 0x50)
    Sleep(1000)
    OP_24(0x125, 0x55)
    Sleep(1000)
    OP_24(0x125, 0x5A)
    Sleep(1000)
    OP_24(0x125, 0x5F)

    def lambda_638():
        OP_8F(0xFE, 0x7C4C, 0x3A98, 0x6338, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_638)
    Sleep(1000)
    OP_24(0x125, 0x64)
    Fade(500)
    OP_6D(-1420, 17640, 19710, 0)
    OP_67(0, 8860, -10000, 0)
    OP_6B(5690, 0)
    OP_6C(146000, 0)
    OP_6E(592, 0)
    Sleep(1000)

    def lambda_6A3():
        OP_6D(8660, 30000, 16320, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A3)

    def lambda_6BB():
        OP_67(0, 12670, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BB)

    def lambda_6D3():
        OP_6B(8100, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D3)
    Sleep(500)

    def lambda_6E8():
        OP_D1(254, 0, 90000, -20000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6E8)
    WaitChrThread(0x10, 0x1)
    Fade(500)

    def lambda_70C():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x15F90, 0x7530, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_70C)
    WaitChrThread(0x10, 0x1)

    def lambda_72D():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x15F90, 0x5DC0, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_72D)
    WaitChrThread(0x10, 0x1)

    def lambda_74E():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x61A8, 0x4E20, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_74E)
    WaitChrThread(0x10, 0x1)

    def lambda_76F():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x4E20, 0x3E80, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_76F)
    WaitChrThread(0x10, 0x1)

    def lambda_790():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x2710, 0x2EE0, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_790)

    def lambda_7AC():
        OP_D1(254, 0, 360000, 0, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7AC)
    WaitChrThread(0x10, 0x1)

    def lambda_7CB():
        OP_97(0x10, 0x64DC, 0xFFFFE9EE, 0x1388, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7CB)
    WaitChrThread(0x10, 0x1)

    def lambda_7EC():
        OP_8F(0x10, 0xFFFFEF7A, 0x3A98, 0xFFFFE21E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7EC)
    WaitChrThread(0x10, 0x1)

    def lambda_80C():
        OP_6D(5290, -2990, 340, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80C)

    def lambda_824():
        OP_67(0, 8860, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_824)

    def lambda_83C():
        OP_6B(5980, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_83C)

    def lambda_84C():
        OP_6C(135000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_84C)

    def lambda_85C():
        OP_6E(592, 8000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_85C)
    SetChrPos(0x10, -4230, 15000, -7650, 0)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x4, 430)
    OP_70(0x4, 0x320)
    OP_43(0x10, 0x3, 0x0, 0x3)

    def lambda_89F():
        OP_8F(0xFE, 0xFFFFEF7A, 0x32, 0xFFFFE21E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_89F)
    Sleep(2500)

    def lambda_8BF():
        OP_8F(0xFE, 0xFFFFEF7A, 0x32, 0xFFFFE21E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8BF)
    Sleep(1500)

    def lambda_8DF():
        OP_8F(0xFE, 0xFFFFEF7A, 0x32, 0xFFFFE21E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8DF)
    OP_22(0xDC, 0x0, 0x64)
    OP_23(0x79)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_E8(0x88, 0x13, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x10, 3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -3600, 0, 22870, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -5550, 0, 18820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -9480, 0, 16660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -8470, 0, 11180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -5930, 0, 13690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -5590, 0, 8880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -9170, 0, 6400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -11620, 0, 3140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -11760, 0, -2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -11440, 0, -6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -9040, 0, -10280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4730, 0, -11890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -5560, 0, -17380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x10, 0x1)
    OP_6F(0x0, 1800)
    OP_70(0x0, 0x73A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_2_399 end

    def Function_3_EB5(): pass

    label("Function_3_EB5")

    Sleep(2400)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(450)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(450)
    Return()

    # Function_3_EB5 end

    def Function_4_ED9(): pass

    label("Function_4_ED9")

    PlayEffect(0x2, 0x5, 0x13, 0, 0, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x13, 0, -150, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_F49():
        OP_8F(0xFE, 0x5762, 0xFFFFF452, 0x5834, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F49)
    Sleep(100)

    def lambda_F69():
        OP_8C(0xFE, 90, 20)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F69)
    Sleep(300)

    def lambda_F7C():
        OP_8C(0xFE, 90, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F7C)

    def lambda_F8A():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_F8A)

    def lambda_F98():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_F98)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)

    def lambda_FB0():
        OP_8F(0xFE, 0x3458, 0xFFFFF452, 0x5906, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB0)
    Sleep(100)

    def lambda_FD0():
        OP_8F(0xFE, 0x3458, 0xFFFFF452, 0x5906, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD0)
    Sleep(3000)

    def lambda_FF0():
        OP_8F(0xFE, 0x3458, 0xFFFFF452, 0x5906, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FF0)
    WaitChrThread(0xFE, 0x1)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    PlayEffect(0x1, 0xFF, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    SetChrSubChip(0xC, 0)
    Sleep(100)
    SetChrSubChip(0xD, 0)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    Sleep(100)

    def lambda_106E():

        label("loc_106E")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_106E")

    QueueWorkItem2(0xC, 2, lambda_106E)

    def lambda_107F():

        label("loc_107F")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_107F")

    QueueWorkItem2(0xD, 2, lambda_107F)

    def lambda_1090():

        label("loc_1090")

        OP_8C(0xFE, 180, 0)
        OP_48()
        Jump("loc_1090")

    QueueWorkItem2(0xE, 2, lambda_1090)
    Return()

    # Function_4_ED9 end

    def Function_5_109C(): pass

    label("Function_5_109C")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    OP_6D(470, 3050, 11510, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(107000, 0)
    OP_6E(348, 0)
    SetChrPos(0x9, -2450, 2550, 7820, 45)
    SetChrPos(0x8, -4050, 2550, 8210, 45)
    SetChrPos(0xA, -4620, 3050, 9670, 45)
    SetChrPos(0xB, -3020, 3050, 9520, 45)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A1(0x13, 0x3)
    SetChrPos(0x13, 9510, -3000, 21510, 67)
    OP_48()
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    OP_89(0xC, 10370, -2960, 21920, 72)
    OP_89(0xD, 9200, -2950, 21540, 162)
    OP_89(0xE, 8220, -2960, 21060, 162)
    SetChrChipByIndex(0xC, 7)
    SetChrSubChip(0xC, 3)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    OP_E5(0xC, 0x0, 0x0)
    OP_E5(0xD, 0x0, 0x0)
    OP_E5(0xE, 0x0, 0x0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 301)
    OP_70(0x3, 0x168)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 6)
    OP_8C(0x14, 45, 0)
    OP_CF(0x14, 0x1, "Frame127_FireEmitter")
    OP_A1(0x12, 0x1)
    SetChrPos(0x12, 24820, -2550, 8060, 285)
    SetChrFlags(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x249F0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\mp032_00.eff")
    LoadEffect(0x1, "map\\mp007_00.eff")
    LoadEffect(0x2, "monster\\ms30703.eff")
    LoadEffect(0x3, "map\\mp013_02.eff")
    LoadEffect(0x4, "map\\mp013_00.eff")
    LoadEffect(0x5, "map\\mp013_01.eff")
    LoadEffect(0x6, "map\\mpsibuk.eff")
    PlayEffect(0x3, 0x5, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x75, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xB, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 5)
    Sleep(1000)
    OP_DC()

    ChrTalk(    #0
        0xB,
        (
            "#151FOh, woooooooow! It's so big!\x02\x03",

            "#150FHe's so handsome, too!\x01",
            "It's a shame he's asleep.\x02\x03",

            "I hope he wakes up soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "#145FI told you, girl, if he wakes up we're\x01",
            "in trouble.\x02\x03",

            "#140FStill...helluva of a creature.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(1000)

    def lambda_16BE():
        OP_6D(430, 2550, 8189, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16BE)

    def lambda_16D6():
        OP_67(0, 6790, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16D6)

    def lambda_16EE():
        OP_6B(2830, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_16EE)

    def lambda_16FE():
        OP_6C(108000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_16FE)

    def lambda_170E():
        OP_6E(364, 3000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_170E)

    def lambda_171E():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_171E)
    Sleep(100)

    def lambda_1731():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1731)
    Sleep(100)

    def lambda_1744():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1744)
    Sleep(100)

    def lambda_1757():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1757)
    OP_43(0x101, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0x105, 0x1, 0x0, 0x9)
    Sleep(300)
    OP_43(0x103, 0x1, 0x0, 0xA)
    Sleep(300)
    OP_43(0x104, 0x1, 0x0, 0xB)
    Sleep(300)
    OP_43(0x108, 0x1, 0x0, 0xC)
    WaitChrThread(0x108, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        "#1018F#2PWow...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #3
        0x103,
        "#023F#2PHmm. 'Incredible' hardly does it justice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        "#151FEstelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        "#141FHeheh, you guys came too, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#161F#5PYour Highness...it is dangerous out here.\x02\x03",

            "Please, I must ask you to return to the cabin.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 400)
    Sleep(300)

    ChrTalk(    #7
        0x105,
        (
            "#045F#2PHaha, I'll be fine, General.\x02\x03",

            "#040FBesides, seeing it up close...\x01",
            "it truly is magnificent.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #8
        0x101,
        "#1015F#2PIs it really asleep, though?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#176F#5PWe've confirmed a heartbeat, so it\x01",
            "isn't dead.\x02\x03",

            "#170FEven so...we pumped enough tranquilizers\x01",
            "into it to stop an army of normal monsters.\x02\x03",

            "It will be down for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1006F#2PCool, that's good, then.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#1004F#2PSpeaking of things being good...\x02\x03",

            "Does anybody see that Leonhardt-Loewe-whoever\x01",
            "guy around?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AA2():
        OP_8C(0xFE, 315, 300)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1AA2)
    Sleep(50)

    def lambda_1AB5():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AB5)
    Sleep(50)
    OP_8C(0x104, 315, 400)
    Sleep(200)

    ChrTalk(    #12
        0x108,
        "#072F#2PHmm. I doubt he could be hiding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x104,
        (
            "#032F#2PLoewe held the Gospel, which was the linchpin\x01",
            "of this experiment.\x02\x03",

            "If he is not here...does that mean they have\x01",
            "abandoned their quest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#170F#5PAccording to the patrol ships that chased the\x01",
            "dragon in, there was never a rider visible.\x02\x03",

            "I'd say it's very likely he wasn't present\x01",
            "to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#163F#5PHmph. Not surprising.\x02\x03",

            "#160FHe probably learned of our plan and fled.\x01",
            "Typical of his sort of criminal element.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F#2PHmm. I dunno, he doesn't seem like the kind\x01",
            "of guy to just turn tail and run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#026F#2PIndeed. We shouldn't let our guard down\x01",
            "just yet.\x02\x03",

            "#020FIncidentally. Where ARE you taking the\x01",
            "dragon after this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#160F#5PFor the moment, the plan is to tow it\x01",
            "to Leiston.\x02\x03",

            "After that, we'll need to discuss it with\x01",
            "Her Majesty and Cassius first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        "#027F#2PI see.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 45, 400)
    Sleep(500)

    ChrTalk(    #20
        0xB,
        "#153F#5PHuuuh?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_1F11():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F11)
    Sleep(50)

    def lambda_1F24():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1F24)
    Sleep(50)

    def lambda_1F37():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1F37)
    Sleep(300)

    ChrTalk(    #21
        0xA,
        "#143F#5PDorothy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1004F#2PDid you find something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        (
            "#154F#5PHmmmm... Maybe it's just my\x01",
            "imagination, buuuuut...\x02\x03",

            "Is there a bump on his forehead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1020F#2PWha...\x02",
    )

    CloseMessageWindow()

    def lambda_1FFE():
        OP_6D(10820, -2990, 12220, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FFE)

    def lambda_2016():
        OP_67(0, 5770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2016)

    def lambda_202E():
        OP_6B(3240, 5000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_202E)

    def lambda_203E():
        OP_6C(116000, 5000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_203E)

    def lambda_204E():
        OP_6E(258, 5000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_204E)

    def lambda_205E():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_205E)

    def lambda_206C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_206C)
    Sleep(80)

    def lambda_207F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_207F)

    def lambda_208D():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_208D)
    Sleep(80)

    def lambda_20A0():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20A0)

    def lambda_20AE():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20AE)
    Sleep(80)

    def lambda_20C1():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20C1)
    Sleep(80)

    def lambda_20D4():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_20D4)
    WaitChrThread(0x105, 0x2)
    Sleep(500)

    ChrTalk(    #25
        0x101,
        (
            "#1004F#5PShe's right. There's this little bump.\x02\x03",

            "#1016FThere's a slit on it, actually.\x01",
            "Maybe it's like an eye or som--\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_72(0x1, 0x20)
    OP_6F(0x1, 370)
    OP_70(0x1, 0x190)
    OP_22(0x211, 0x0, 0x64)
    OP_73(0x1)
    Fade(500)
    OP_6D(-530, 2550, 7580, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(96000, 0)
    OP_6E(316, 0)
    OP_0D()

    ChrTalk(    #26
        0x101,
        "#1020F#2PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        "#042F#5PNo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x108,
        "#077F#2PThe Gospel! It's here!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x14, -700, 1000, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#1002F#2P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "#162F#2PHm?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_DB()
    OP_1D(0x2D)
    Sleep(200)
    Fade(500)
    OP_6D(-20890, 24910, 27240, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(117000, 0)
    OP_6E(393, 0)
    OP_82(0x1, 0x2)
    OP_0D()
    OP_6F(0x1, 410)
    OP_70(0x1, 0x1AE)
    Sleep(800)
    OP_22(0x195, 0x0, 0x64)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 430)
    OP_70(0x1, 0x1C2)
    OP_43(0x13, 0x3, 0x0, 0xD)
    OP_22(0x128, 0x0, 0x64)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_E8(0x88, 0x13, 0x0, 0x0)
    PlayEffect(0x6, 0xFF, 0xFF, 15370, -2990, 13060, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 13970, -2990, 15960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 18150, -2990, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 18080, -2990, 15980, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 17330, -2990, 17950, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 17340, -2990, 19770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 17580, -2990, 21340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 19480, -2990, 22570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 21630, -2990, 24490, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 23880, -2990, 26250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 26120, -2990, 28050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 28120, -2990, 27060, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 27960, -2990, 23990, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 24680, -2990, 11900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 39640, -2990, 1370, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 39400, -2990, 4550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 36700, -2990, 5030, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 21270, -2990, -2410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 20050, -2990, -5190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 18770, -2990, -8060, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 15030, -2990, -9420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 12190, -2990, -9520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 10510, -2990, -7130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 9840, -2990, -4250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 10850, -2990, -940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 12660, -2990, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 13230, -2990, 4340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 15410, -2990, 5750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 17030, -2990, 6320, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 15860, -2990, 7910, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 14220, -2990, 8830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 11220, -2990, 7340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 11280, -2990, 10620, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 11240, -2990, 13590, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_72(0x1, 0x20)
    OP_73(0x1)
    OP_6F(0x1, 450)
    OP_70(0x1, 0x1F4)
    OP_56(0x0)

    def lambda_2A5C():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A5C)

    def lambda_2A77():
        OP_6D(-4430, 27000, 22590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A77)

    def lambda_2A8F():
        OP_67(0, 5870, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A8F)

    def lambda_2AA7():
        OP_6E(470, 3000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AA7)
    Sleep(2200)
    Fade(500)
    LoadEffect(0x6, "map\\mp007_00.eff")
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_D8(0x1, 0x1F4)
    OP_B0(0x1, 0xA)
    OP_6F(0x1, 650)
    OP_70(0x1, 0x29E)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_22(0x195, 0x0, 0x64)
    OP_7C(0x1F4, 0x1F4, 0x1388, 0x1F4)
    OP_7C(0x12C, 0x12C, 0x1388, 0x1F4)
    PlayEffect(0x2, 0xFF, 0x14, 1000, 1000, 0, 90, -90, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)

    def lambda_2B66():
        OP_6D(-90, 22490, 20940, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B66)

    def lambda_2B7E():
        OP_67(0, 4820, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B7E)

    def lambda_2B96():
        OP_6C(128000, 1500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B96)

    def lambda_2BA6():
        OP_6B(1820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2BA6)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F6)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_109C end

    def Function_6_2BE1(): pass

    label("Function_6_2BE1")

    Sleep(700)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x64)
    Sleep(2100)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x64)
    Return()

    # Function_6_2BE1 end

    def Function_7_2C1E(): pass

    label("Function_7_2C1E")

    OP_22(0x1F6, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F6, 0x0, 0x64)
    Return()

    # Function_7_2C1E end

    def Function_8_2C38(): pass

    label("Function_8_2C38")

    SetChrPos(0xFE, -4170, 2550, 1210, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEEC6, 0x9F6, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF790, 0x9F6, 0x1784, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_8_2C38 end

    def Function_9_2C7E(): pass

    label("Function_9_2C7E")

    SetChrPos(0xFE, -4170, 2550, 1210, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEEC6, 0x9F6, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF15A, 0x9F6, 0x1842, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF650, 0x9F6, 0x1A9A, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x14, 400)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_9_2C7E end

    def Function_10_2CDF(): pass

    label("Function_10_2CDF")

    SetChrPos(0xFE, -4170, 2550, 1210, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEEC6, 0x9F6, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF6F0, 0x9F6, 0x13A6, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_10_2CDF end

    def Function_11_2D25(): pass

    label("Function_11_2D25")

    SetChrPos(0xFE, -4170, 2550, 1210, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEEC6, 0x9F6, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF0B0, 0x9F6, 0x1888, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_11_2D25 end

    def Function_12_2D6B(): pass

    label("Function_12_2D6B")

    SetChrPos(0xFE, -4170, 2550, 1210, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEEC6, 0x9F6, 0xB5E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF10A, 0x9F6, 0x13EC, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_12_2D6B end

    def Function_13_2DB1(): pass

    label("Function_13_2DB1")

    OP_82(0x5, 0x2)
    PlayEffect(0x4, 0x6, 0x13, 0, -100, 2200, 0, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x7, 0x13, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_2E24():
        OP_8F(0xFE, 0x1248, 0xFFFFF452, 0x6BE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2E24)

    def lambda_2E3F():
        OP_8C(0xFE, 0, 100)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2E3F)
    Sleep(200)
    SetChrChipByIndex(0xD, 11)
    SetChrSubChip(0xD, 0)
    Sleep(100)
    SetChrChipByIndex(0xE, 11)
    SetChrSubChip(0xE, 0)
    WaitChrThread(0x13, 0x2)
    OP_8C(0xD, 180, 400)
    OP_8C(0xE, 180, 400)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    PlayEffect(0x3, 0x5, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_13_2DB1 end

    def Function_14_2EB4(): pass

    label("Function_14_2EB4")

    EventBegin(0x0)
    OP_6D(-2009, 4490, 8140, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(227000, 0)
    OP_6E(268, 0)
    SetChrPos(0x101, -2160, 2550, 6020, 45)
    SetChrPos(0x103, -2320, 2550, 5030, 45)
    SetChrPos(0x105, -2480, 2550, 6810, 45)
    SetChrPos(0x104, -3920, 2550, 6280, 45)
    SetChrPos(0x108, -3830, 2550, 5100, 45)
    SetChrPos(0x9, -2450, 2550, 7820, 45)
    SetChrPos(0x8, -3730, 2550, 7850, 45)
    SetChrPos(0xA, -4620, 3050, 9670, 45)
    SetChrPos(0xB, -3020, 3050, 9520, 45)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_22(0x75, 0x1, 0x50)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #31
        0x101,
        "#1020F#5PWaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#162F#5PDamn you... You will not escape!\x02\x03",

            "Schwarz! Get us in the air!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #33
        0x8,
        "#177F#2PSir!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1A24)
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2EB4 end

    def Function_15_313D(): pass

    label("Function_15_313D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    SetChrBattleFlags(0x17, 0x20)
    SetChrBattleFlags(0x18, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    OP_89(0x17, -5390, 1550, -16510, 135)
    OP_89(0x18, -2410, 1550, -15670, 135)
    OP_89(0x16, -5090, 1550, -12910, 315)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x8, -5260, 2550, 6560, 68)
    SetChrPos(0x15, -3970, 2550, 6620, 273)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_6D(-5540, 2140, -8240, 0)
    OP_67(0, 7350, -10000, 0)
    OP_6B(5670, 0)
    OP_6C(37000, 0)
    OP_6E(395, 0)
    OP_43(0x18, 0x1, 0x0, 0x10)
    OP_43(0x16, 0x1, 0x0, 0x11)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC16._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_3282():
        OP_6D(-4280, 2550, 6090, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3282)

    def lambda_329A():
        OP_67(0, 6070, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_329A)

    def lambda_32B2():
        OP_6B(5290, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_32B2)

    def lambda_32C2():
        OP_6C(126000, 7000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_32C2)

    def lambda_32D2():
        OP_6E(331, 7000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_32D2)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_313D end

    def Function_16_3313(): pass

    label("Function_16_3313")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3391")
    OP_8E(0xFE, 0xFFFFF7D6, 0x60E, 0xFFFFCC02, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(700)
    OP_8E(0xFE, 0xFFFFF6BE, 0x60E, 0xFFFFD4CC, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 45, 400)
    Sleep(700)
    OP_8E(0xFE, 0xFFFFF696, 0x60E, 0xFFFFC2CA, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(700)
    Jump("Function_16_3313")

    label("loc_3391")

    Return()

    # Function_16_3313 end

    def Function_17_3392(): pass

    label("Function_17_3392")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3429")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFFE41C, 0x60E, 0xFFFFD436, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(600)
    OP_8E(0xFE, 0xFFFFEC1E, 0x60E, 0xFFFFCD92, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(800)
    OP_8E(0xFE, 0xFFFFF2AE, 0x60E, 0xFFFFD440, 0x7D0, 0x0)
    Sleep(800)
    OP_8E(0xFE, 0xFFFFEC1E, 0x60E, 0xFFFFCD92, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(800)
    Jump("Function_17_3392")

    label("loc_3429")

    Return()

    # Function_17_3392 end

    SaveToFile()

Try(main)
