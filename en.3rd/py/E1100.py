from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1100   ._SN',
        MapName             = 'event',
        Location            = 'E1100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60170",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Man in Black',                         # 9
        'Man in Black',                         # 10
        'Dummy Character',                      # 11
        'Dummy Character',                      # 12
        'Dummy Character',                      # 13
        'Dummy Character',                      # 14
        'Dummy Character',                      # 15
        'Steel Cougar',                         # 16
        'Steel Cougar',                         # 17
        'Merkabah',                             # 18
        'Aldan',                                # 19
        'Aldan',                                # 20
        'Noble Woman',                          # 21
        'Masked Man',                           # 22
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


    AddCharChip(
        'ED6_DT27/CH04080 ._CH',             # 00
        'ED6_DT27/CH03420 ._CH',             # 01
        'ED6_DT27/CH03460 ._CH',             # 02
        'ED6_DT27/CH04420 ._CH',             # 03
        'ED6_DT27/CH04421 ._CH',             # 04
        'ED6_DT27/CH04460 ._CH',             # 05
        'ED6_DT27/CH04461 ._CH',             # 06
        'ED6_DT26/CH20613 ._CH',             # 07
        'ED6_DT29/CH12330 ._CH',             # 08
        'ED6_DT29/CH12331 ._CH',             # 09
        'ED6_DT26/CH20600 ._CH',             # 0A
        'ED6_DT26/CH20618 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH02870 ._CH',             # 0D
        'ED6_DT07/CH02850 ._CH',             # 0E
        'ED6_DT26/CH20685 ._CH',             # 0F
        'ED6_DT26/CH20686 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT27/CH04080P._CP',             # 00
        'ED6_DT27/CH03420P._CP',             # 01
        'ED6_DT27/CH03460P._CP',             # 02
        'ED6_DT27/CH04420P._CP',             # 03
        'ED6_DT27/CH04421P._CP',             # 04
        'ED6_DT27/CH04460P._CP',             # 05
        'ED6_DT27/CH04461P._CP',             # 06
        'ED6_DT26/CH20613P._CP',             # 07
        'ED6_DT29/CH12330P._CP',             # 08
        'ED6_DT29/CH12331P._CP',             # 09
        'ED6_DT26/CH20600P._CP',             # 0A
        'ED6_DT26/CH20618P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH02870P._CP',             # 0D
        'ED6_DT07/CH02850P._CP',             # 0E
        'ED6_DT26/CH20685P._CP',             # 0F
        'ED6_DT26/CH20686P._CP',             # 10
    )

    DeclNpc(
        X                   = -1320,
        Z                   = 0,
        Y                   = -42890,
        Direction           = 180,
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
        X                   = 610,
        Z                   = 0,
        Y                   = -42950,
        Direction           = 180,
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
        X                   = -6490,
        Z                   = 0,
        Y                   = 27360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6710,
        Z                   = 0,
        Y                   = 26220,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6960,
        Z                   = 0,
        Y                   = 27190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7900,
        Z                   = 0,
        Y                   = 29550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8780,
        Z                   = 0,
        Y                   = 29670,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1320,
        Z                   = 0,
        Y                   = -42890,
        Direction           = 180,
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
        X                   = 610,
        Z                   = 0,
        Y                   = -42950,
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xC4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17580,
        Z                   = 1250,
        Y                   = -23660,
        Direction           = 234,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -17580,
        Z                   = 1250,
        Y                   = -23660,
        Direction           = 234,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -19070,
        Z                   = 1250,
        Y                   = 25620,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -19070,
        Z                   = 1250,
        Y                   = 24320,
        Direction           = 282,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )


    DeclEvent(
        X                   = -15540,
        Y                   = -1000,
        Z                   = -15260,
        Range               = -3080,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFCC84,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_4E2",          # 01, 1
        "Function_2_56C",          # 02, 2
        "Function_3_582",          # 03, 3
        "Function_4_598",          # 04, 4
        "Function_5_5FF",          # 05, 5
        "Function_6_9D6",          # 06, 6
        "Function_7_A34",          # 07, 7
        "Function_8_A8A",          # 08, 8
        "Function_9_A9D",          # 09, 9
        "Function_10_DB5",         # 0A, 10
        "Function_11_DE5",         # 0B, 11
        "Function_12_E10",         # 0C, 12
        "Function_13_106B",        # 0D, 13
        "Function_14_108C",        # 0E, 14
        "Function_15_1332",        # 0F, 15
        "Function_16_182A",        # 10, 16
        "Function_17_1D08",        # 11, 17
        "Function_18_1D66",        # 12, 18
        "Function_19_20EE",        # 13, 19
        "Function_20_229E",        # 14, 20
    )


    def Function_0_312(): pass

    label("Function_0_312")

    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F")
    Event(0, 9)

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_36E")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_3FE")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_38D")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_3FE")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3AC")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_3FE")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_END)), "loc_3E2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 14500, 0, 39890, 180)
    SetChrPos(0x11, 15970, 0, 39960, 180)
    Jump("loc_3FE")

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3FE")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 0)), scpexpr(EXPR_END)), "loc_4BF")
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, -7000, 0, 26580, 0)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 11)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -8410, 0, 29780, 90)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_4E1")
    SetChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_43(0x1B, 0x1, 0x0, 0x4)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)

    label("loc_4E1")

    Return()

    # Function_0_312 end

    def Function_1_4E2(): pass

    label("Function_1_4E2")

    OP_22(0x1C3, 0x0, 0x64)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    OP_B1("E1100_2")
    Jump("loc_508")

    label("loc_4FF")

    OP_B1("E1100_1")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_51D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_51D")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545")
    OP_72(0x201A, 0x0)
    ExitThread()
    OP_72(0x81A, 0x0)
    ExitThread()
    OP_6F(0x1A, 0)
    OP_71(0x419, 0x0)
    ExitThread()
    Jump("loc_55F")

    label("loc_545")

    OP_72(0x2019, 0x0)
    ExitThread()
    OP_72(0x819, 0x0)
    ExitThread()
    OP_6F(0x19, 0)
    OP_70(0x19, 0x0)

    label("loc_55F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_END)), "loc_56B")
    OP_22(0x79, 0x1, 0x5A)

    label("loc_56B")

    Return()

    # Function_1_4E2 end

    def Function_2_56C(): pass

    label("Function_2_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("Function_2_56C")

    label("loc_581")

    Return()

    # Function_2_56C end

    def Function_3_582(): pass

    label("Function_3_582")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597")
    OP_99(0xFE, 0x0, 0x7, 0x1388)
    Jump("Function_3_582")

    label("loc_597")

    Return()

    # Function_3_582 end

    def Function_4_598(): pass

    label("Function_4_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FE")
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x1B, 270, 800)
    Sleep(300)
    OP_8C(0x1B, 90, 800)
    Sleep(500)
    OP_8C(0x1B, 180, 800)
    Sleep(300)
    OP_8C(0x1B, 225, 800)
    Sleep(500)
    OP_8C(0x1B, 135, 800)
    Sleep(300)
    OP_8C(0x1B, 0, 800)
    Sleep(500)
    Jump("Function_4_598")

    label("loc_5FE")

    Return()

    # Function_4_598 end

    def Function_5_5FF(): pass

    label("Function_5_5FF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C0(0x28, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DC(0x2, 0xFF)
    OP_DC(0x1, 0x0, 0x8)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    OP_DC(0x1, 0x0, 0x8)
    OP_DB(0x0, 0x8)
    Call(6, 8)
    OP_A2(0x2501)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_BB(0x1, 0x1, 0x1A)
    OP_BB(0x2, 0x1, 0x19)
    OP_BB(0x3, 0x1, 0x1B)
    OP_BB(0x4, 0x1, 0x1D)
    OP_BB(0x8, 0x1, 0x17)
    OP_BD()
    OP_C2(0x1, 0x1F)
    SetChrFlags(0x109, 0x80)
    OP_6D(21810, -22000, 99940, 0)
    OP_67(0, -3000, -10000, 0)
    OP_6B(7080, 0)
    OP_6C(339000, 0)
    OP_6E(712, 0)
    OP_23(0x79)
    OP_11(0x0, 0x15, 0x32, 0xC350, 0x48058, 0x0)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0xFFEC, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS530._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(5000)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    Sleep(1500)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0xFFF6, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS531._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    Sleep(5000)
    OP_C6(0x1, 0x3, 16777215, 1500, 0)
    Sleep(2000)
    OP_22(0x79, 0x1, 0x0)
    FadeToBright(2000, 0)
    OP_43(0x109, 0x0, 0x0, 0x7)

    def lambda_794():
        OP_6D(10010, -13000, -80310, 17000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_794)

    def lambda_7AC():
        OP_67(0, -4650, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7AC)

    def lambda_7C4():
        OP_6B(7080, 16000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7C4)

    def lambda_7D4():
        OP_6C(339000, 16000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_7D4)

    def lambda_7E4():
        OP_6E(712, 16000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7E4)
    Sleep(4500)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS532._CH")
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(5000)
    OP_C6(0x2, 0x3, 16777215, 1500, 0)
    Sleep(3000)
    Fade(1000)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    StopSound(0x33450, 0x57E40, 0x0)
    OP_24(0x79, 0x50)
    OP_6D(-4300, -4150, 11400, 0)
    OP_67(0, 10770, -10000, 0)
    OP_6B(10680, 0)
    OP_6C(135000, 0)
    OP_6E(655, 0)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x1)

    def lambda_8C0():
        OP_6B(12060, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_8C0)

    def lambda_8D0():
        OP_6E(635, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D0)
    OP_0D()
    OP_C8(0x80, 0x46, "C_PLAC30._CH", 0x0, 0x3E8)
    WaitChrThread(0x10, 0x2)
    Sleep(2000)
    OP_1F(0x0, 0x0)
    OP_1D(0xAA)
    StopSound(0xC350, 0x48058, 0x1D4C0)

    def lambda_915():
        OP_6D(9250, -27700, 24900, 12000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_915)

    def lambda_92D():
        OP_67(0, 6360, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_92D)

    def lambda_945():
        OP_6B(11610, 12000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_945)

    def lambda_955():
        OP_6C(159000, 12000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_955)

    def lambda_965():
        OP_6E(362, 12000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_965)
    Sleep(1000)
    OP_1F(0x64, 0x2710)
    Sleep(2000)
    OP_43(0x109, 0x0, 0x0, 0x8)
    WaitChrThread(0x10, 0x0)

    def lambda_991():
        OP_6B(10610, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_991)

    def lambda_9A1():
        OP_6E(352, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9A1)
    Sleep(2000)
    OP_43(0x109, 0x0, 0x0, 0x6)
    SetMapFlags(0x2000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_5FF end

    def Function_6_9D6(): pass

    label("Function_6_9D6")

    OP_24(0x79, 0x5A)
    Sleep(300)
    OP_24(0x79, 0x50)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x1E)
    Sleep(300)
    OP_24(0x79, 0x14)
    Sleep(300)
    OP_24(0x79, 0xA)
    Sleep(300)
    OP_24(0x79, 0x0)
    Sleep(300)
    OP_23(0x79)
    Return()

    # Function_6_9D6 end

    def Function_7_A34(): pass

    label("Function_7_A34")

    OP_24(0x79, 0xA)
    Sleep(300)
    OP_24(0x79, 0x14)
    Sleep(300)
    OP_24(0x79, 0x1E)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x50)
    Sleep(300)
    OP_24(0x79, 0x5A)
    Sleep(300)
    OP_24(0x79, 0x64)
    Return()

    # Function_7_A34 end

    def Function_8_A8A(): pass

    label("Function_8_A8A")

    Sleep(1000)
    OP_24(0x79, 0x5A)
    Sleep(1000)
    OP_24(0x79, 0x64)
    Return()

    # Function_8_A8A end

    def Function_9_A9D(): pass

    label("Function_9_A9D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -5130, 100, 29750, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -8630, 0, 17670, 0)
    SetChrPos(0x11, -10200, 0, 17890, 0)
    OP_6D(-4010, 100, 30910, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    def lambda_B56():
        OP_6D(-6360, 100, 28560, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B56)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_BCE():
        OP_6D(-4430, 100, 30560, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCE)

    def lambda_BE6():
        OP_67(0, 5240, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BE6)

    def lambda_BFE():
        OP_6B(2900, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BFE)

    def lambda_C0E():
        OP_6E(226, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C0E)
    SetChrChipByIndex(0x11, 6)

    def lambda_C23():
        OP_8F(0xFE, 0xFFFFE6F6, 0x64, 0x71DE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C23)
    Sleep(30)
    SetChrChipByIndex(0x10, 4)

    def lambda_C48():
        OP_8F(0xFE, 0xFFFFE872, 0x64, 0x6EA0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C48)
    WaitChrThread(0x109, 0x0)
    Battle(0x76, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, -7000, 0, 26580, 0)
    ClearChrFlags(0x11, 0x80)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 11)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x800)
    SetChrPos(0x11, -8410, 0, 29780, 90)
    SetChrPos(0x109, -5950, 100, 29570, 225)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-5950, 100, 29570, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A2(0x25E8)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_A9D end

    def Function_10_DB5(): pass

    label("Function_10_DB5")

    Sleep(200)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0xFFFFDD32, 0x0, 0x627A, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 600)
    Return()

    # Function_10_DB5 end

    def Function_11_DE5(): pass

    label("Function_11_DE5")

    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0xFFFFD7CE, 0x0, 0x657C, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 600)
    Return()

    # Function_11_DE5 end

    def Function_12_E10(): pass

    label("Function_12_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 1)), scpexpr(EXPR_END)), "loc_E1B")
    Return()

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E24")
    Return()

    label("loc_E24")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-8650, 0, -12510, 0)
    OP_67(0, 7950, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    SetChrPos(0x109, -9540, 0, -13320, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    def lambda_EB0():

        label("loc_EB0")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_EB0")

    QueueWorkItem2(0x17, 3, lambda_EB0)

    def lambda_EC3():

        label("loc_EC3")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_EC3")

    QueueWorkItem2(0x18, 3, lambda_EC3)
    SetChrPos(0x17, -8310, 0, -31230, 0)
    SetChrPos(0x18, -10300, 0, -31320, 0)

    def lambda_EF8():
        OP_6D(-8420, 0, -20110, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EF8)
    WaitChrThread(0x109, 0x0)
    SetChrChipByIndex(0x17, 9)

    def lambda_F1A():
        OP_8F(0xFE, 0xFFFFDECC, 0x0, 0xFFFFC54A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_F1A)
    Sleep(150)
    SetChrChipByIndex(0x18, 9)

    def lambda_F3F():
        OP_8F(0xFE, 0xFFFFD828, 0x0, 0xFFFFC4FA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_F3F)
    OP_43(0x18, 0x3, 0x0, 0xD)
    Sleep(800)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)

    def lambda_F75():
        OP_6D(-8660, 0, -14310, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F75)

    def lambda_F8D():
        OP_67(0, 7950, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F8D)

    def lambda_FA5():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FA5)

    def lambda_FB5():
        OP_6E(230, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_FB5)
    WaitChrThread(0x109, 0x0)
    Battle(0x77, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x18, 0x3)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x109, -9350, 0, -14440, 180)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-9350, 0, -14440, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25E9)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_E10 end

    def Function_13_106B(): pass

    label("Function_13_106B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_108B")
    OP_22(0x13F, 0x0, 0x50)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(300)
    Jump("Function_13_106B")

    label("loc_108B")

    Return()

    # Function_13_106B end

    def Function_14_108C(): pass

    label("Function_14_108C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(10450, -9000, 56050, 0)
    OP_67(0, 5110, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(248000, 0)
    OP_6E(380, 0)
    OP_C4(0x0, 0x20000)
    SetChrPos(0x109, 10620, -9000, 55300, 0)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x2000)
    ClearChrFlags(0x109, 0x1)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 8)
    OP_A1(0x19, 0x19)
    OP_72(0x419, 0x0)
    ExitThread()
    SetChrPos(0x19, 40000, -50460, 35000, 0)
    ClearChrFlags(0x19, 0x100)
    OP_D1(25, 0, 0, 20000, 0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_22(0x96, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x134, 0x0, 0x64)
    OP_B0(0x1A, 0x28)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0x78)
    Sleep(100)

    def lambda_1191():
        OP_96(0xFE, 0x6978, 0xFFFF61F4, 0x109A0, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1191)
    Sleep(100)

    def lambda_11B4():
        OP_6D(27000, -40460, 68000, 1700)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_11B4)

    def lambda_11CC():
        OP_67(0, -6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11CC)

    def lambda_11E4():
        OP_6B(3200, 1800)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11E4)

    def lambda_11F4():
        OP_6C(257000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_11F4)

    def lambda_1204():
        OP_6E(450, 1800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1204)
    Sleep(200)
    SetChrSubChip(0x109, 9)

    def lambda_121E():
        OP_6D(27000, -40460, 68000, 1300)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_121E)
    Sleep(150)
    SetChrSubChip(0x109, 10)

    def lambda_1240():
        OP_D1(25, -30000, -15000, 60000, 1100)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1240)
    OP_98(0x0, 0x19)
    OP_98(0x1, 0x80E8, 0xFFFF61F4, 0x11170)
    OP_98(0x1, 0xFFFFB1E0, 0x1CC, 0x186A0)
    OP_98(0x1, 0xFFFF15A0, 0x4E20, 0x7530)

    def lambda_1288():
        OP_98(0x2, 0xFE, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1288)
    OP_22(0x2D4, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)
    WaitChrThread(0x109, 0x1)
    SetChrFlags(0x109, 0x80)
    OP_43(0x19, 0x3, 0x0, 0x11)

    def lambda_12B3():
        OP_6B(5500, 6000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_12B3)

    def lambda_12C3():
        OP_6E(650, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_12C3)

    def lambda_12D3():
        OP_D1(25, -20000, -140000, 70000, 1800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_12D3)
    OP_73(0x1A)
    OP_71(0x41A, 0x0)
    ExitThread()

    def lambda_12F6():
        OP_D1(25, -20000, -160000, 30000, 2500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_12F6)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_C4(0x1, 0x20000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_108C end

    def Function_15_1332(): pass

    label("Function_15_1332")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    BlurSwitch(0x0, 0x60FFFFFF, 0x0, 0x1, 0x5)
    ClearMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(10450, -9000, 56050, 0)
    OP_67(0, 5110, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(248000, 0)
    OP_6E(380, 0)
    LoadEffect(0x0, "scraft\\sc000_33.eff")
    OP_C4(0x0, 0x20000)
    OP_72(0x201A, 0x0)
    ExitThread()
    OP_72(0x81A, 0x0)
    ExitThread()
    OP_6F(0x1A, 0)
    SetChrPos(0x109, 10620, -9000, 55300, 0)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x109, 0x2000)
    ClearChrFlags(0x109, 0x1)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 8)
    OP_A1(0x19, 0x19)
    OP_71(0x419, 0x0)
    ExitThread()
    SetChrPos(0x19, 15000, -114000, 100000, 0)
    ClearChrFlags(0x19, 0x100)
    OP_D1(25, -10000, 130000, -30000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x134, 0x0, 0x64)
    OP_B0(0x1A, 0x28)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0x78)
    Sleep(100)

    def lambda_1464():
        OP_96(0xFE, 0x9C40, 0xFFFE7960, 0x124F8, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1464)
    Sleep(100)

    def lambda_1487():

        label("loc_1487")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1487")

    QueueWorkItem2(0x109, 3, lambda_1487)

    def lambda_14A2():
        OP_6D(28000, -46000, 70000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_14A2)

    def lambda_14BA():
        OP_67(0, -6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_14BA)

    def lambda_14D2():
        OP_6B(3000, 1800)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_14D2)

    def lambda_14E2():
        OP_6C(260000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_14E2)

    def lambda_14F2():
        OP_6E(380, 1800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_14F2)
    Sleep(200)
    SetChrSubChip(0x109, 9)
    Sleep(1200)
    OP_6D(42140, -101460, 75000, 0)
    OP_67(0, -18390, -10000, 0)
    OP_6B(1960, 0)
    OP_6C(253000, 0)
    OP_6E(672, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_22(0x96, 0x1, 0x64)
    SetChrSubChip(0x109, 2)

    def lambda_1592():
        OP_8F(0xFE, 0xB1BC, 0xFFFE5250, 0x128E0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1592)

    def lambda_15AD():

        label("loc_15AD")

        OP_7C(0x64, 0x64, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_15AD")

    QueueWorkItem2(0x109, 3, lambda_15AD)

    def lambda_15C8():
        OP_6D(42140, -101460, 75000, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_15C8)

    def lambda_15E0():
        OP_67(0, -18390, -10000, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15E0)

    def lambda_15F8():
        OP_6B(10, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_15F8)

    def lambda_1608():
        OP_6C(260000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1608)

    def lambda_1618():
        OP_6E(1300, 5000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1618)

    def lambda_1628():
        OP_D0(7000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1628)
    OP_71(0x41A, 0x0)
    ExitThread()
    Sleep(1500)
    OP_22(0x2D4, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)
    Sleep(300)
    OP_72(0x419, 0x0)
    ExitThread()

    def lambda_1658():
        OP_8F(0xFE, 0x11170, 0xFFFE42B0, 0xE290, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1658)
    Sleep(500)
    OP_82(0x0, 0x0)
    SetChrFlags(0x109, 0x80)
    Sleep(300)
    OP_43(0x19, 0x3, 0x0, 0x11)

    def lambda_168C():
        OP_6D(-40980, -73250, 80350, 2500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_168C)

    def lambda_16A4():
        OP_67(0, -8540, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16A4)

    def lambda_16BC():
        OP_6B(2000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_16BC)

    def lambda_16CC():
        OP_6C(140000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16CC)

    def lambda_16DC():
        OP_6E(1065, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_16DC)
    Sleep(1000)
    OP_71(0x419, 0x0)
    ExitThread()
    OP_44(0x19, 0x1)
    SetChrPos(0x19, 0, -60000, 120000, 0)
    OP_72(0x419, 0x0)
    ExitThread()

    def lambda_1712():
        OP_D1(25, 0, 160000, -20000, 1000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1712)
    OP_98(0x0, 0x19)
    OP_98(0x1, 0x186A0, 0xFFFFB1E0, 0xFFFFB1E0)
    OP_98(0x1, 0xFFFF3CB0, 0x0, 0xFFFE7960)
    OP_98(0x1, 0xFFFCF2C0, 0x9C40, 0xFFFDB610)

    def lambda_175A():
        OP_98(0x2, 0xFE, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_175A)
    Sleep(1000)

    def lambda_176F():
        OP_D1(25, -15000, 180000, -40000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_176F)

    def lambda_1789():
        OP_6D(-40980, -73250, 80350, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1789)

    def lambda_17A1():
        OP_67(0, -8540, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17A1)

    def lambda_17B9():
        OP_6B(2100, 8000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_17B9)

    def lambda_17C9():
        OP_6C(140000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_17C9)

    def lambda_17D9():
        OP_6E(1165, 8000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17D9)
    Sleep(2000)

    def lambda_17EE():
        OP_D1(25, -5000, 240000, -60000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_17EE)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_C4(0x1, 0x20000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1332 end

    def Function_16_182A(): pass

    label("Function_16_182A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(10450, -9000, 56050, 0)
    OP_67(0, 5110, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(248000, 0)
    OP_6E(380, 0)
    LoadEffect(0x0, "scraft\\sc000_33.eff")
    OP_C4(0x0, 0x20000)
    SetChrPos(0x109, 10620, -9000, 55300, 0)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrFlags(0x109, 0x2000)
    ClearChrFlags(0x109, 0x1)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 8)
    OP_A1(0x19, 0x19)
    OP_71(0x419, 0x0)
    ExitThread()
    SetChrPos(0x19, 16000, -103000, 100000, 0)
    ClearChrFlags(0x19, 0x100)
    OP_D1(25, -10000, 130000, -30000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x134, 0x0, 0x64)
    OP_B0(0x1A, 0x28)
    OP_6F(0x1A, 0)
    OP_70(0x1A, 0x78)
    Sleep(100)

    def lambda_1940():
        OP_96(0xFE, 0x9C40, 0xFFFE7960, 0x124F8, 0x2BC, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1940)
    Sleep(100)

    def lambda_1963():

        label("loc_1963")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1963")

    QueueWorkItem2(0x109, 3, lambda_1963)

    def lambda_197E():
        OP_6D(28000, -46000, 70000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_197E)

    def lambda_1996():
        OP_67(0, -6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1996)

    def lambda_19AE():
        OP_6B(3000, 1800)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_19AE)

    def lambda_19BE():
        OP_6C(260000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_19BE)

    def lambda_19CE():
        OP_6E(380, 1800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19CE)
    Sleep(200)
    SetChrSubChip(0x109, 9)
    Sleep(1200)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x1)
    OP_44(0x109, 0x1)
    OP_6D(42140, -101460, 75000, 0)
    OP_67(0, -18390, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(250000, 0)
    OP_6E(672, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_22(0x96, 0x1, 0x64)
    SetChrPos(0x109, 50000, -100000, 76000, 0)
    SetChrSubChip(0x109, 2)

    def lambda_1A97():
        OP_8F(0xFE, 0x9C40, 0xFFFE7960, 0x124F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A97)

    def lambda_1AB2():

        label("loc_1AB2")

        OP_7C(0x64, 0x64, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1AB2")

    QueueWorkItem2(0x109, 3, lambda_1AB2)

    def lambda_1ACD():
        OP_6B(400, 3500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1ACD)

    def lambda_1ADD():
        OP_6C(260000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1ADD)

    def lambda_1AED():
        OP_6E(1400, 3500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AED)

    def lambda_1AFD():
        OP_D0(7000, 5000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1AFD)
    OP_71(0x41A, 0x0)
    ExitThread()
    Sleep(3000)
    OP_22(0x2D4, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)
    Sleep(300)
    OP_72(0x419, 0x0)
    ExitThread()

    def lambda_1B2D():
        OP_8F(0xFE, 0x105B8, 0xFFFE7384, 0xC350, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1B2D)
    Sleep(500)
    OP_82(0x0, 0x0)
    SetChrFlags(0x109, 0x80)
    Sleep(300)
    OP_43(0x19, 0x3, 0x0, 0x11)

    def lambda_1B61():
        OP_6D(-40980, -73250, 80350, 2500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1B61)

    def lambda_1B79():
        OP_67(0, -8540, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B79)

    def lambda_1B91():
        OP_6B(2000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1B91)

    def lambda_1BA1():
        OP_6C(140000, 2500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1BA1)

    def lambda_1BB1():
        OP_6E(1065, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BB1)
    Sleep(1000)
    OP_71(0x419, 0x0)
    ExitThread()
    OP_44(0x19, 0x1)
    SetChrPos(0x19, 0, -60000, 120000, 0)
    OP_72(0x419, 0x0)
    ExitThread()

    def lambda_1BE7():
        OP_D1(25, 0, 160000, -20000, 1000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BE7)
    OP_98(0x0, 0x19)
    OP_98(0x1, 0x186A0, 0xFFFFB1E0, 0xFFFFB1E0)
    OP_98(0x1, 0xFFFF3CB0, 0x0, 0xFFFE7960)
    OP_98(0x1, 0xFFFCF2C0, 0x9C40, 0xFFFDB610)

    def lambda_1C2F():
        OP_98(0x2, 0xFE, 0x13880, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1C2F)
    Sleep(1000)

    def lambda_1C44():
        OP_D1(25, -20000, 190000, -40000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1C44)

    def lambda_1C5E():
        OP_6D(-40980, -73250, 80350, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1C5E)

    def lambda_1C76():
        OP_67(0, -8540, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1C76)

    def lambda_1C8E():
        OP_6B(2100, 8000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1C8E)

    def lambda_1C9E():
        OP_6C(140000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1C9E)

    def lambda_1CAE():
        OP_6E(1165, 8000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1CAE)
    Sleep(2000)

    def lambda_1CC3():
        OP_D1(25, -5000, 240000, -60000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1CC3)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_C4(0x1, 0x20000)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_182A end

    def Function_17_1D08(): pass

    label("Function_17_1D08")

    OP_24(0x2D5, 0x5A)
    Sleep(300)
    OP_24(0x2D5, 0x50)
    Sleep(300)
    OP_24(0x2D5, 0x46)
    Sleep(300)
    OP_24(0x2D5, 0x3C)
    Sleep(300)
    OP_24(0x2D5, 0x32)
    Sleep(300)
    OP_24(0x2D5, 0x28)
    Sleep(300)
    OP_24(0x2D5, 0x1E)
    Sleep(300)
    OP_24(0x2D5, 0x14)
    Sleep(300)
    OP_24(0x2D5, 0xA)
    Sleep(300)
    OP_24(0x2D5, 0x0)
    Sleep(300)
    OP_23(0x2D5)
    Return()

    # Function_17_1D08 end

    def Function_18_1D66(): pass

    label("Function_18_1D66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_1D9C")

    ChrTalk(    #0
        0xFE,
        "Aaaaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Someone, help!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EA5")

    label("loc_1D9C")


    ChrTalk(    #2
        0xFE,
        (
            "Affording the ticket to come on here today sure\x01",
            "wasn't cheap...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I had to sell photographs for ages to gather up\x01",
            "enough...and now that money's all gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "So I've REALLY got to make the most of tonight...\x01",
            "Let's make this a night to remember, Lusitania!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA5")

    Jump("loc_20EA")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_1FCF")

    ChrTalk(    #5
        0xFE,
        "Wh-What's going on here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "W-We're not gonna crash, are we?! \x01",
            "You wouldn't fall outta the air on me,\x01",
            "would you, Lusitania?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x109,
        "Kevin Graham",
        (
            "#1079F(Poor guy missed his chance to run away.)\x02\x03",

            "#1075F(There's something familiar about him...\x01",
            "but, well, I'd best leave him alone.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E7")

    label("loc_1FCF")


    ChrTalk(    #8
        0xFE,
        "Oh, Lusitania, why are you so beautiful?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I do wish your top speed was a little faster\x01",
            "than 1,000 APH...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "...but nothing can beat you when it comes\x01",
            "to sheer size or capacity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Fitting a whole thousand people on board isn't\x01",
            "something any other airships can boast!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E7")

    OP_A2(0x0)

    label("loc_20EA")

    TalkEnd(0xFE)
    Return()

    # Function_18_1D66 end

    def Function_19_20EE(): pass

    label("Function_19_20EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_216B")

    ChrTalk(    #12
        0xFE,
        (
            "I'm so grateful I was able to see you today\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Truly, I am, but if Father were to find out...\x02",
    )

    CloseMessageWindow()
    Jump("loc_229A")

    label("loc_216B")

    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)

    ChrTalk(    #14
        0x1D,
        (
            "I'm sorry for calling you out here out of\x01",
            "nowhere like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1D,
        "But I so, so wanted to meet with you...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1C, 225, 500)

    ChrTalk(    #16
        0x1C,
        (
            "But... But then you came all the way on this ship\x01",
            "just for that?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x1C, 270, 620)

    ChrTalk(    #17
        0x1C,
        (
            "Y-You do know what will happen if my father finds\x01",
            "out, don't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_A2(0x1)

    label("loc_229A")

    TalkEnd(0xFE)
    Return()

    # Function_19_20EE end

    def Function_20_229E(): pass

    label("Function_20_229E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_238D")

    ChrTalk(    #18
        0xFE,
        (
            "Haha. I know he doesn't approve of me because\x01",
            "of my social standing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "...but I must beg that you let me overstretch\x01",
            "myself and act the part of a bigger man today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "At least for as long as I have this mask on...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2391")

    label("loc_238D")

    Call(0, 19)

    label("loc_2391")

    TalkEnd(0xFE)
    Return()

    # Function_20_229E end

    SaveToFile()

Try(main)
