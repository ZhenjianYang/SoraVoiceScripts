from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0810   ._SN',
        MapName             = 'Event',
        Location            = 'E0810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Airship',                              # 9
        'Airship',                              # 10
        'Ancient Dragon',                       # 11
        'Strange Monster',                      # 12
        'Target Camera',                        # 13
        'Mary',                                 # 14
        'Strange Monster',                      # 15
        'Mary',                                 # 16
        'Gilbert',                              # 17
        'Prince Olivert',                       # 18
        'Major Vander',                         # 19
        'Chancellor Osborne',                   # 20
        'Secretary Lechter',                    # 21
        'Erika',                                # 22
        'Dan',                                  # 23
        'Target Character',                     # 24
        'Dummy Camera',                         # 25
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
        'ED6_DT29/CH14373 ._CH',             # 00
        'ED6_DT29/CH14800 ._CH',             # 01
        'ED6_DT27/CH03260 ._CH',             # 02
        'ED6_DT27/CH03570 ._CH',             # 03
        'ED6_DT27/CH03950 ._CH',             # 04
        'ED6_DT26/CH20805 ._CH',             # 05
        'ED6_DT27/CH04267 ._CH',             # 06
        'ED6_DT27/CH04269 ._CH',             # 07
        'ED6_DT27/CH04262 ._CH',             # 08
        'ED6_DT26/CH20809 ._CH',             # 09
        'ED6_DT26/CH20758 ._CH',             # 0A
        'ED6_DT26/CH20759 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14373P._CP',             # 00
        'ED6_DT29/CH14800P._CP',             # 01
        'ED6_DT27/CH03260P._CP',             # 02
        'ED6_DT27/CH03570P._CP',             # 03
        'ED6_DT27/CH03950P._CP',             # 04
        'ED6_DT26/CH20805P._CP',             # 05
        'ED6_DT27/CH04267P._CP',             # 06
        'ED6_DT27/CH04269P._CP',             # 07
        'ED6_DT27/CH04262P._CP',             # 08
        'ED6_DT26/CH20809P._CP',             # 09
        'ED6_DT26/CH20758P._CP',             # 0A
        'ED6_DT26/CH20759P._CP',             # 0B
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x1A4,
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
        NpcIndex            = 0x1A4,
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
        NpcIndex            = 0x1A4,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E4,
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
        NpcIndex            = 0xEE,
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
        NpcIndex            = 0xEE,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_4AD",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_51D",          # 03, 3
        "Function_4_73D",          # 04, 4
        "Function_5_78D",          # 05, 5
        "Function_6_D88",          # 06, 6
        "Function_7_DCD",          # 07, 7
        "Function_8_DE0",          # 08, 8
        "Function_9_E35",          # 09, 9
        "Function_10_E9A",         # 0A, 10
        "Function_11_111A",        # 0B, 11
        "Function_12_15C3",        # 0C, 12
        "Function_13_1814",        # 0D, 13
        "Function_14_1E2C",        # 0E, 14
        "Function_15_1F36",        # 0F, 15
        "Function_16_1F7A",        # 10, 16
        "Function_17_1FCF",        # 11, 17
        "Function_18_1FF6",        # 12, 18
        "Function_19_26B3",        # 13, 19
        "Function_20_278C",        # 14, 20
        "Function_21_27E9",        # 15, 21
        "Function_22_28C6",        # 16, 22
        "Function_23_28DD",        # 17, 23
        "Function_24_28F4",        # 18, 24
        "Function_25_2927",        # 19, 25
        "Function_26_2CBB",        # 1A, 26
        "Function_27_42E0",        # 1B, 27
        "Function_28_439B",        # 1C, 28
        "Function_29_44DC",        # 1D, 29
        "Function_30_451B",        # 1E, 30
        "Function_31_4698",        # 1F, 31
        "Function_32_46CE",        # 20, 32
        "Function_33_46F3",        # 21, 33
        "Function_34_4BFC",        # 22, 34
        "Function_35_4C65",        # 23, 35
        "Function_36_4CE9",        # 24, 36
        "Function_37_53D8",        # 25, 37
        "Function_38_54B9",        # 26, 38
        "Function_39_5542",        # 27, 39
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    OP_A3(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_353")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 36)
    Jump("loc_36A")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_36A")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 33)

    label("loc_36A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_393")
    OP_A3(0x2509)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_415")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_3AD")
    OP_A3(0x2508)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_415")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_3CA")
    OP_A3(0x2507)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1)
    Event(0, 12)
    Jump("loc_415")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_3E4")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_415")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3FE")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_415")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_415")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)

    label("loc_415")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_43D")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_43D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_45C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_45C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_484")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 26)

    label("loc_484")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_4AC")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 25)

    label("loc_4AC")

    Return()

    # Function_0_32A end

    def Function_1_4AD(): pass

    label("Function_1_4AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CE")
    OP_B1("E0810_1")
    Jump("loc_4ED")

    label("loc_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4E4")
    OP_A3(0x1)
    OP_B1("E0810_1")
    Jump("loc_4ED")

    label("loc_4E4")

    OP_B1("E0810_0")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_506")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_506")

    Return()

    # Function_1_4AD end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_507")

    label("loc_51C")

    Return()

    # Function_2_507 end

    def Function_3_51D(): pass

    label("Function_3_51D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_A1(0x10, 0x5)
    SetChrPos(0x10, -30000, 0, -10000, 90)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-32710, 6500, 41650, 0)
    OP_67(0, 3100, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(315000, 0)
    OP_6E(527, 0)

    def lambda_5AD():
        OP_6D(-30160, 10500, 10250, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5AD)

    def lambda_5C5():
        OP_67(0, 1240, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5C5)

    def lambda_5DD():
        OP_6B(6760, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5DD)

    def lambda_5ED():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_5ED)

    def lambda_5FD():
        OP_6E(704, 10000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5FD)

    def lambda_60D():
        OP_91(0xFE, 0x0, 0x1388, 0x493E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_60D)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5500)
    OP_44(0x0, 0x0)
    OP_43(0x0, 0x0, 0x0, 0x4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x20000000)
    OP_44(0x10, 0x0)
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x0, 0x0)
    Sleep(1000)
    OP_F7(0xA, 0x4, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00Side Story [Departure] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")
    Sleep(1000)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x4, 0x20)
    OP_3E(0x2CF, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Received \x1F\xCF\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(8000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #2
        "\x07\x05Received \x07\x028,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_730")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5505   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_51D end

    def Function_4_73D(): pass

    label("Function_4_73D")

    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x79, 0x0)
    OP_23(0x79)
    Return()

    # Function_4_73D end

    def Function_5_78D(): pass

    label("Function_5_78D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x80)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -75210, 5050, -18190, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_1D(0x1)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        (
            "\x07\x00Western Calvard, bordering Liberl...\x02\x03",

            "2,200 arge above ground level...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(-208950, -12600, -29370, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(10830, 0)
    OP_6C(292000, 0)
    OP_6E(550, 0)
    FadeToBright(2000, 0)

    def lambda_907():
        OP_6E(610, 7000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_907)
    Sleep(1000)

    def lambda_91C():
        OP_6D(-110390, 7000, 14140, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_91C)

    def lambda_934():
        OP_67(0, 1000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_934)

    def lambda_94C():
        OP_6B(8770, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_94C)

    def lambda_95C():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_95C)
    WaitChrThread(0x10B, 0x0)
    OP_43(0x12, 0x1, 0x0, 0x6)

    def lambda_978():
        OP_6D(-80390, 4000, 15140, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_978)

    def lambda_990():
        OP_67(0, 1600, -10000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_990)

    def lambda_9A8():
        OP_6B(15000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_9A8)

    def lambda_9B8():
        OP_6C(45000, 16000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_9B8)

    QueueWorkItem(0x12, 0, None)
    OP_43(0x10, 0x1, 0x0, 0x9)

    def lambda_9D5():
        OP_91(0xFE, 0xFFFFC568, 0xFFFFF830, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9D5)
    WaitChrThread(0x10, 0x0)

    def lambda_9F5():
        OP_91(0xFE, 0xFFFFB9B0, 0x7D0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_9F5)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10, 0x1)

    def lambda_A1A():
        OP_91(0xFE, 0x2710, 0xFFFFF830, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A1A)

    def lambda_A35():
        OP_D1(254, 0, 270000, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A35)
    WaitChrThread(0x10, 0x3)

    def lambda_A54():
        OP_D1(254, 0, 270000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A54)
    WaitChrThread(0x10, 0x0)

    def lambda_A73():
        OP_D1(254, -10000, 250000, 60000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_A73)
    OP_43(0x12, 0x1, 0x0, 0x7)

    def lambda_A94():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A94)
    Sleep(100)

    def lambda_AB4():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AB4)
    Sleep(100)

    def lambda_AD4():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AD4)
    Sleep(100)

    def lambda_AF4():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AF4)
    Sleep(100)

    def lambda_B14():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B14)
    Sleep(100)

    def lambda_B34():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B34)
    Sleep(100)

    def lambda_B54():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B54)
    Sleep(100)

    def lambda_B74():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B74)
    Sleep(100)

    def lambda_B94():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B94)
    Sleep(100)

    def lambda_BB4():
        OP_8F(0xFE, 0xFFF85EE0, 0x11170, 0xFFF85EE0, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BB4)
    Sleep(1500)
    OP_44(0x10B, 0x0)
    OP_44(0x10B, 0x1)
    OP_44(0x10B, 0x2)
    OP_44(0x10B, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x3)
    SetChrPos(0x10, -59790, -5000, -4880, 270)
    OP_D1(16, 0, 270000, -30000, 0)
    OP_6D(-101260, -10100, 8020, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(4130, 0)
    OP_6C(269000, 0)
    OP_6E(869, 0)
    OP_D0(-25000, 0)

    def lambda_C56():
        OP_D1(254, 0, 270000, 25000, 4000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_C56)

    def lambda_C70():
        OP_6D(-71660, -10100, -8530, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_C70)

    def lambda_C88():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_C88)

    def lambda_CA0():
        OP_6B(6000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_CA0)
    Sleep(2000)

    def lambda_CB5():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_CB5)
    OP_24(0x79, 0x5A)
    WaitChrThread(0x10B, 0x0)
    WaitChrThread(0x10B, 0x1)
    WaitChrThread(0x10B, 0x2)
    WaitChrThread(0x10B, 0x3)

    def lambda_CDD():
        OP_D1(254, 0, 270000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_CDD)

    def lambda_CF7():
        OP_6D(-62000, -5550, 1720, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_CF7)

    def lambda_D0F():
        OP_67(0, 5780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_D0F)

    def lambda_D27():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_D27)

    def lambda_D37():
        OP_D0(0, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_D37)
    WaitChrThread(0x10B, 0x0)
    Sleep(1000)

    def lambda_D51():
        OP_6E(700, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_D51)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_43(0x12, 0x1, 0x0, 0x8)
    OP_0D()
    OP_44(0x10B, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_5_78D end

    def Function_6_D88(): pass

    label("Function_6_D88")

    OP_22(0x79, 0x1, 0xA)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x50)
    Return()

    # Function_6_D88 end

    def Function_7_DCD(): pass

    label("Function_7_DCD")

    Sleep(800)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Return()

    # Function_7_DCD end

    def Function_8_DE0(): pass

    label("Function_8_DE0")

    OP_24(0x79, 0x5A)
    Sleep(150)
    OP_24(0x79, 0x50)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0xA)
    Sleep(150)
    OP_23(0x79)
    Return()

    # Function_8_DE0 end

    def Function_9_E35(): pass

    label("Function_9_E35")

    Sleep(1000)
    OP_D1(16, 0, 270000, 5000, 1500)
    OP_D1(16, 0, 270000, -10000, 800)
    OP_D1(16, 0, 270000, 0, 1000)
    OP_D1(16, 0, 270000, 15000, 1300)
    OP_D1(16, 0, 270000, 0, 1000)
    Return()

    # Function_9_E35 end

    def Function_10_E9A(): pass

    label("Function_10_E9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x8)
    OP_6D(-53740, 25000, 17680, 0)
    OP_67(0, 1340, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -37600, 25000, -54800, 0)
    FadeToBright(2000, 0)

    def lambda_F25():
        OP_6D(-37600, 25980, -54830, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_F25)

    def lambda_F3D():
        OP_6C(190000, 5000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_F3D)

    def lambda_F4D():
        OP_8C(0xFE, 45, 5000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F4D)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)
    WaitChrThread(0x10B, 0x0)
    Sleep(300)

    NpcTalk(    #4
        0x18,
        "Blue-Haired Jaeger",
        "Hmph... Not bad for a bunch of silly ex-bandits.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x18,
        "Blue-Haired Jaeger",
        (
            "But their luck is now about to run out--after all,\x01",
            "no one stands a chance against the almighty\x01",
            "Gilbert!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1065():
        OP_6B(3700, 1000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1065)

    def lambda_1075():
        OP_6C(218000, 1000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1075)
    WaitChrThread(0x10B, 0x0)
    Sleep(500)

    ChrTalk(    #6
        0x18,
        (
            "#1226FOnward, G-Apache!\x02\x03",

            "#1225FIt's time to shoot down the Bobcat!\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10E5():
        OP_6B(0, 1500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10E5)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x2507)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_E9A end

    def Function_11_111A(): pass

    label("Function_11_111A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    SetChrFlags(0x10B, 0x8)
    SetChrFlags(0x10B, 0x4)
    SetChrPos(0x10B, -37600, 25000, -54800, 0)
    OP_6D(-37600, 25800, -54800, 0)
    OP_67(0, 1340, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -37600, 25000, -54800, 0)
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\\\mp009_00.eff")
    LoadEffect(0x2, "map\\\\mpsmk0.eff")
    LoadEffect(0x3, "Scraft\\\\sc000_31.eff")
    PlayEffect(0x2, 0x0, 0x18, 500, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x18, 1500, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x18, -1000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x18, 0, 0, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_12DA():
        OP_9E(0xFE, 0x14, 0xFFFFFFFB, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_12DA)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x64)

    def lambda_12FE():
        OP_6B(4200, 2000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12FE)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #7
        0x18,
        (
            "#1224F#5PTh-This can't be happening... How could my\x01",
            "G-Apache be defeated?!\x02\x03",

            "#1225FWhere's the p-parachute?! Is this it?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0xFFFFFCF4, 1820, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x18)
    Sleep(500)

    ChrTalk(    #8
        0x18,
        (
            "#1227F#5P#3S...NO! This is the button to deploy the\x01",
            "big 'victory is mine!' flag!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x18, 0x20)
    OP_4A(0x18, 255)
    OP_23(0x77)
    OP_23(0x135)
    OP_22(0x13B, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x18, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x18, 1500, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x4, 0x18, -1500, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0x18, 0, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    def lambda_1521():
        OP_6D(-37600, 8800, -54800, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1521)

    def lambda_1539():
        OP_67(0, 5860, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1539)

    def lambda_1551():
        OP_6B(14200, 4000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1551)

    def lambda_1561():
        OP_8F(0xFE, 0xFFFF6D20, 0xFFFFD8F0, 0xFFFF29F0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1561)
    Sleep(400)

    ChrTalk(    #9 op#A
        0x18,
        "#5P#15A#4SNoooooooooooooooooo!#2S\x02",
    )

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(3000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_111A end

    def Function_12_15C3(): pass

    label("Function_12_15C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10B, 0x80)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_6D(71500, 0, 0, 0)
    OP_67(0, 1120, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(90000, 0)
    OP_6E(760, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x64)
    OP_A1(0x10, 0x6)
    SetChrPos(0x10, 120000, 0, 0, 0)
    ClearChrFlags(0x10, 0x100)
    OP_D1(16, 0, 270000, 0, 0)
    OP_71(0x2006, 0x0)
    ExitThread()
    OP_6F(0x6, 800)
    OP_70(0x6, 0x384)

    def lambda_16C5():
        OP_8F(0xFE, 0xC350, 0x0, 0x0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_16C5)
    FadeToBright(2000, 0)
    WaitChrThread(0x10, 0x0)

    def lambda_16EE():
        OP_6D(-26420, 0, -20260, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_16EE)

    def lambda_1706():
        OP_6C(134000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1706)

    def lambda_1716():
        OP_6B(8460, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1716)

    def lambda_1726():
        OP_D0(-6000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_1726)

    def lambda_1736():
        OP_D1(254, 0, 250000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1736)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0x0, 0x0, 0x0)
    OP_98(0x1, 0xFFFF8AD0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFEDB08)

    def lambda_177E():
        OP_98(0x2, 0xFE, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_177E)
    WaitChrThread(0x10, 0x0)

    def lambda_1793():
        OP_8F(0xFE, 0xFFFEEE90, 0x0, 0xFFFBBA40, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1793)
    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_23(0x79)
    OP_0D()
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_15C3 end

    def Function_13_1814(): pass

    label("Function_13_1814")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_6D(-61040, -10000, -5750, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(9240, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x10B, 0x80)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -75210, 15000, -18190, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_6D(-49710, -11090, -210, 0)
    OP_67(0, 8470, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(57000, 0)
    OP_6E(1056, 0)

    def lambda_1948():
        OP_6D(-58000, -11090, 40, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1948)

    def lambda_1960():
        OP_67(0, 9070, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1960)

    def lambda_1978():
        OP_6B(4850, 6000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1978)
    OP_22(0x79, 0x1, 0x64)
    LoadEffect(0x1, "map\\mp077_00.eff")
    LoadEffect(0x2, "map\\mp096_00.eff")
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_19BD():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_19BD)
    OP_72(0x2003, 0x0)
    ExitThread()
    OP_D8(0x3, 0x3E8)
    OP_B0(0x3, 0x2)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x154)
    OP_73(0x1)
    OP_B0(0x3, 0x1E)
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_6F(0x3, 240)
    OP_70(0x3, 0x154)
    WaitChrThread(0x10, 0x0)

    def lambda_1A14():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A14)
    Sleep(200)

    def lambda_1A34():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A34)
    Sleep(200)

    def lambda_1A54():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A54)
    Sleep(200)

    def lambda_1A74():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A74)
    Sleep(200)

    def lambda_1A94():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A94)
    Sleep(200)

    def lambda_1AB4():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AB4)
    Sleep(200)

    def lambda_1AD4():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AD4)
    Sleep(200)

    def lambda_1AF4():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AF4)
    Sleep(200)

    def lambda_1B14():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1B14)
    Sleep(200)

    def lambda_1B34():
        OP_8F(0xFE, 0xFFF9E580, 0x3A98, 0xFFFFB8F2, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1B34)
    Sleep(100)
    OP_44(0x10B, 0x0)
    OP_44(0x10B, 0x1)
    OP_44(0x10B, 0x2)
    OP_44(0x10, 0x0)
    SetChrPos(0x10, -70210, 20000, -5190, 0)
    OP_D1(16, 0, 270000, 45000, 0)
    OP_43(0x10, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x2, 0x0, 0x11)
    OP_6D(-119800, 10800, -21040, 0)
    OP_67(0, -4100, -10000, 0)
    OP_6B(7010, 0)
    OP_6C(303000, 0)
    OP_6E(628, 0)

    def lambda_1BD3():
        OP_6C(250000, 11000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1BD3)

    def lambda_1BE3():
        OP_6D(-94100, 19500, -19610, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1BE3)

    def lambda_1BFB():
        OP_67(0, -4070, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1BFB)

    def lambda_1C13():
        OP_6B(4850, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1C13)

    def lambda_1C23():
        OP_6E(689, 2500)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_1C23)
    WaitChrThread(0x10B, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, -75320, 20000, -30020, 40, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_1C6D():
        OP_6D(-185440, -14150, -8840, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 0, lambda_1C6D)

    def lambda_1C85():
        OP_67(0, 8250, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1C85)

    def lambda_1C9D():
        OP_6B(10770, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1C9D)

    def lambda_1CAD():
        OP_6E(869, 8000)
        ExitThread()

    QueueWorkItem(0x10B, 3, lambda_1CAD)
    Sleep(4000)
    PlayEffect(0x1, 0xFF, 0xFF, -205000, -10000, -2610, 270, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -208000, -11000, 2610, 270, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -212450, -12000, 11610, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, -216450, -13000, 15610, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x12, 0x1, 0x0, 0x10)
    Sleep(1500)
    OP_C4(0x1, 0x20000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x1C3)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_F7(0xB, 0x1, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00Side Story [Capua's Delivery Service] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Call(0, 14)
    Return()

    # Function_13_1814 end

    def Function_14_1E2C(): pass

    label("Function_14_1E2C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDD")
    OP_28(0x24, 0x4, 0x20)
    OP_3E(0x2CE, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Received \x1F\xCE\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDD")
    OP_35(0xA, 0x112)
    OP_BB(0xA, 0x6, 0x112)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Josette learned the S-Craft\x01",
            "\x07\x02[Bobcat]\x07\x05.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1E")
    OP_28(0x24, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x05Received \x07\x023,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_1F1E")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1E2C end

    def Function_15_1F36(): pass

    label("Function_15_1F36")

    Sleep(1000)
    OP_98(0x0, 0x10)
    OP_98(0x1, 0xFFFE2A6E, 0x3A98, 0xFFFF6302)
    OP_98(0x1, 0xFFFCF1EE, 0xFFFFD8F0, 0xFFFFD832)
    OP_98(0x1, 0xFFFBB96E, 0xFFFF3CB0, 0xEB1E)

    def lambda_1F6F():
        OP_98(0x2, 0xFE, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F6F)
    Return()

    # Function_15_1F36 end

    def Function_16_1F7A(): pass

    label("Function_16_1F7A")

    OP_24(0x79, 0x5A)
    Sleep(150)
    OP_24(0x79, 0x50)
    Sleep(150)
    OP_24(0x79, 0x46)
    Sleep(150)
    OP_24(0x79, 0x3C)
    Sleep(150)
    OP_24(0x79, 0x32)
    Sleep(150)
    OP_24(0x79, 0x28)
    Sleep(150)
    OP_24(0x79, 0x1E)
    Sleep(150)
    OP_24(0x79, 0x14)
    Sleep(150)
    OP_24(0x79, 0xA)
    Sleep(150)
    OP_23(0x79)
    Return()

    # Function_16_1F7A end

    def Function_17_1FCF(): pass

    label("Function_17_1FCF")

    OP_D1(16, 0, 270000, 0, 2500)
    OP_D1(16, -30000, 310000, -40000, 4000)
    Return()

    # Function_17_1FCF end

    def Function_18_1FF6(): pass

    label("Function_18_1FF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x100000)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    ClearMapFlags(0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x14E, 0x4)
    SetChrFlags(0x14E, 0x8)
    SetChrPos(0x14E, 0, 0, 0, 270)
    SetChrPos(0x13, 0, -1500, 0, 270)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x15, 0, -900, 0, 270)
    SetChrPos(0x16, 0, -1500, 0, 270)
    SetChrPos(0x17, 0, -1300, 0, 270)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_22(0x1C3, 0x1, 0x64)
    OP_43(0x15, 0x0, 0x0, 0x13)
    OP_43(0x16, 0x0, 0x0, 0x13)
    OP_43(0x17, 0x0, 0x0, 0x13)
    OP_43(0x13, 0x2, 0x0, 0x14)
    OP_43(0x14E, 0x3, 0x0, 0x16)
    OP_6D(-45010, 12700, -18610, 0)
    OP_67(0, 1210, -10000, 0)
    OP_6B(4450, 0)
    OP_6C(33000, 0)
    OP_6E(417, 0)

    def lambda_218C():
        OP_6D(-13310, 8000, -17410, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_218C)

    def lambda_21A4():
        OP_67(0, 3220, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_21A4)

    def lambda_21BC():
        OP_6B(4340, 6000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_21BC)

    def lambda_21CC():
        OP_6E(341, 6000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_21CC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x20, 0x0)
    Fade(1000)
    OP_6D(0, 0, 0, 0)
    OP_67(0, 4480, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(294, 0)
    OP_43(0x14E, 0x3, 0x0, 0x17)
    OP_0D()
    Sleep(300)

    ChrTalk(    #14
        0x15,
        "#1714F#2PY-You saved me...!\x02",
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x13, 0xFFFFFE0C, 2000, 0x8, 0x9, 0xC8, 0x5)
    Sleep(2000)
    OP_63(0x13)

    ChrTalk(    #15
        0x15,
        "#1714F#2PYou can fly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x16,
        "#3PI'm still a kid, so yup-yup!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x15,
        "#1714F#2PCan you only fly if you're little?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x16,
        "#3PWell, no. Grownups can, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x16,
        "#3PIt just causes, uhh...problems...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0xC8, 2800, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #20
        0x15,
        "#1714F#2PTh-That's not much of an answer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x16,
        "#3PHaha...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2396():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2396)
    Sleep(200)

    def lambda_23B6():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23B6)
    Sleep(200)

    def lambda_23D6():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23D6)
    Sleep(200)

    def lambda_23F6():
        OP_8F(0xFE, 0xFFFFC568, 0x7D0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_23F6)
    WaitChrThread(0x13, 0x1)
    SetChrPos(0x13, 0, 5000, 15000, 270)
    Fade(1000)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFA, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFF7, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFEC, 0xFFFFFFFA, 0x0, 0x0, 0x0)
    OP_6D(-22600, 4000, 0, 0)
    OP_67(0, 1140, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(270000, 0)
    OP_6E(456, 0)
    OP_43(0x13, 0x3, 0x0, 0x15)
    OP_0D()
    Sleep(500)

    def lambda_24BB():
        OP_6D(-46340, 3000, -2840, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_24BB)

    def lambda_24D3():
        OP_6C(310000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_24D3)

    def lambda_24E3():
        OP_6E(320, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_24E3)
    WaitChrThread(0x13, 0x3)

    def lambda_24F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_24F8)

    def lambda_250A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14E, 0, lambda_250A)
    Sleep(1000)
    Fade(1000)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x14E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x14E, 0, 0, 0, 270)
    SetChrPos(0x13, 0, -1500, 0, 270)
    OP_6D(0, 0, 0, 0)
    OP_67(0, 240, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(270000, 0)
    OP_6E(284, 0)
    OP_D0(6000, 0)
    OP_0D()
    FadeToDark(4000, 16777215, -126)
    OP_0D()

    def lambda_25B0():
        OP_6B(3100, 15000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_25B0)

    NpcTalk(    #22
        0x16,
        "Voice",
        "Today sure was fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x17,
        "#1714F#5P...What?\x02",
    )

    CloseMessageWindow()

    def lambda_25F6():
        OP_6B(3600, 10000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_25F6)
    OP_44(0x14E, 0x3)
    Sleep(1000)
    OP_20(0x1388)
    FadeToDark(4000, 16777215, -1)
    OP_43(0x14E, 0x3, 0x0, 0x18)
    OP_24(0x1C3, 0x5A)
    Sleep(400)
    OP_24(0x1C3, 0x50)
    Sleep(400)
    OP_24(0x1C3, 0x46)
    Sleep(400)
    OP_24(0x1C3, 0x3C)
    Sleep(400)
    OP_24(0x1C3, 0x32)
    Sleep(400)
    OP_24(0x1C3, 0x28)
    Sleep(400)
    OP_24(0x1C3, 0x1E)
    Sleep(400)
    OP_24(0x1C3, 0x14)
    OP_0D()
    Sleep(1000)
    OP_21()
    OP_23(0x1C3)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_44(0x14, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapFlags(0x10)
    ClearChrFlags(0x14E, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2101   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1FF6 end

    def Function_19_26B3(): pass

    label("Function_19_26B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278B")
    OP_44(0x13, 0x2)

    def lambda_26C6():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_26C6)
    Sleep(355)

    def lambda_26DB():
        OP_91(0xFE, 0x0, 0xFFFFFF9C, 0x0, 0xDC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26DB)
    Sleep(485)
    OP_44(0xFE, 0x1)
    SetChrPos(0x15, 0, -1000, 0, 270)
    SetChrPos(0x16, 0, -1600, 0, 270)
    SetChrPos(0x17, 0, -1400, 0, 270)
    Sleep(185)

    def lambda_2737():
        OP_91(0xFE, 0x0, 0x64, 0x0, 0xFA, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2737)
    Sleep(315)
    OP_44(0xFE, 0x1)
    SetChrPos(0x15, 0, -900, 0, 270)
    SetChrPos(0x16, 0, -1500, 0, 270)
    SetChrPos(0x17, 0, -1300, 0, 270)
    Jump("Function_19_26B3")

    label("loc_278B")

    Return()

    # Function_19_26B3 end

    def Function_20_278C(): pass

    label("Function_20_278C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27E8")
    SetChrSubChip(0xFE, 2)
    Sleep(167)
    SetChrSubChip(0xFE, 3)
    Sleep(168)
    SetChrSubChip(0xFE, 4)
    Sleep(167)
    SetChrSubChip(0xFE, 5)
    Sleep(168)
    SetChrSubChip(0xFE, 6)
    Sleep(167)
    SetChrSubChip(0xFE, 7)
    Sleep(168)
    SetChrSubChip(0xFE, 0)
    Sleep(167)
    SetChrSubChip(0xFE, 1)
    Sleep(168)
    Jump("Function_20_278C")

    label("loc_27E8")

    Return()

    # Function_20_278C end

    def Function_21_27E9(): pass

    label("Function_21_27E9")

    OP_97(0x13, 0x0, 0x0, 0xFFFEA070, 0x2710, 0x0)
    OP_97(0x13, 0xFFFF9E58, 0x0, 0x15F90, 0x2710, 0x0)
    OP_62(0x13, 0x96, 2450, 0x26, 0x27, 0xC8, 0x2)

    def lambda_282B():
        OP_8F(0xFE, 0xFFFF3CB0, 0x5DC, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_282B)
    WaitChrThread(0x13, 0x1)

    def lambda_284B():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_284B)
    Sleep(200)

    def lambda_286B():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_286B)
    Sleep(200)

    def lambda_288B():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_288B)
    Sleep(200)

    def lambda_28AB():
        OP_8F(0xFE, 0xFFFEEE90, 0xDAC, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_28AB)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_21_27E9 end

    def Function_22_28C6(): pass

    label("Function_22_28C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28DC")
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1400)
    Jump("Function_22_28C6")

    label("loc_28DC")

    Return()

    # Function_22_28C6 end

    def Function_23_28DD(): pass

    label("Function_23_28DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28F3")
    OP_22(0x120, 0x0, 0x46)
    Sleep(1400)
    Jump("Function_23_28DD")

    label("loc_28F3")

    Return()

    # Function_23_28DD end

    def Function_24_28F4(): pass

    label("Function_24_28F4")

    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1300)
    Return()

    # Function_24_28F4 end

    def Function_25_2927(): pass

    label("Function_25_2927")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_22(0x1C3, 0x0, 0x64)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_A1(0x10, 0x4)
    OP_A1(0x11, 0x5)
    OP_D1(16, 0, 270000, -15000, 0)
    OP_D1(17, 0, 270000, -10000, 0)
    SetChrPos(0x10, 30000, 0, 10000, 0)
    SetChrPos(0x11, 35000, 500, 14000, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 30300, 0, 10000, 270)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 35300, 500, 14000, 270)
    LoadEffect(0x1, "map\\\\mp065_01.eff")
    OP_6D(12820, -4000, -3150, 0)
    OP_67(0, 2380, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(207000, 0)
    OP_6E(860, 0)
    OP_D0(10000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x113, 0x1, 0x14)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)

    def lambda_2A99():
        OP_6D(-14040, -4000, -3150, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2A99)

    def lambda_2AB1():
        OP_6C(227000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2AB1)

    def lambda_2AC1():
        OP_6B(2760, 3000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2AC1)

    def lambda_2AD1():
        OP_D0(-10000, 3000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2AD1)
    PlayEffect(0x1, 0x1, 0x10, -800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x10, 800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2B4B():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2B4B)

    def lambda_2B65():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFFD8F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B65)

    def lambda_2B80():
        OP_8F(0xFE, 0xFFFE7A8C, 0x0, 0xFFFFD8F0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2B80)
    PlayEffect(0x1, 0x3, 0x11, -800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x11, 800, -1700, -300, 0, 90, 90, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2C05():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2C05)

    def lambda_2C1F():
        OP_8F(0xFE, 0xFFFE7960, 0x1F4, 0xFFFFE890, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C1F)

    def lambda_2C3A():
        OP_8F(0xFE, 0xFFFE7A8C, 0x1F4, 0xFFFFE890, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2C3A)
    Sleep(3000)
    OP_24(0x113, 0x64)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(20)
    OP_24(0x113, 0x14)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_23(0x113)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2927 end

    def Function_26_2CBB(): pass

    label("Function_26_2CBB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C3, 0x0, 0x64)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_22(0x79, 0x1, 0x46)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp296_00.eff")
    LoadEffect(0x4, "map\\\\mp296_01.eff")
    LoadEffect(0x1, "map\\\\mp297_00.eff")
    LoadEffect(0x2, "map\\\\mp077_00.eff")
    LoadEffect(0x3, "battle\\btgun00.eff")
    LoadEffect(0x5, "map\\\\mp296_04.eff")
    OP_A1(0x10, 0x2)
    SetChrPos(0x10, 197210, -30000, 8810, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, -15000, 270000, 4000, 0)
    OP_71(0x2002, 0x0)
    ExitThread()
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_B0(0x2, 0x1E)
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, -75210, 10000, -18190, 0)
    ClearChrFlags(0x11, 0x100)
    OP_8C(0x11, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1B, 0x20)
    SetChrBattleFlags(0x1C, 0x20)
    ClearChrFlags(0x1B, 0x1)
    ClearChrFlags(0x1C, 0x1)
    SetChrPos(0x1B, -71180, 17200, -15000, 0)
    SetChrPos(0x1C, -70420, 17200, -16100, 0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x403, 0x0)
    ExitThread()
    OP_6D(-115120, 17200, -18290, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(5860, 0)
    OP_6C(270000, 0)
    OP_6E(334, 0)

    def lambda_2EC6():
        OP_6D(-73000, 17200, -18040, 14000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2EC6)

    def lambda_2EDE():
        OP_6C(225000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EDE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x14, 0x0)
    Fade(1000)
    OP_6D(-71580, 17200, -16360, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #24
        0x1B,
        (
            "#1485F#5PHaha. I'm rather impressed with how Prince\x01",
            "Olivert has come along.\x02\x03",

            "#1481FNo matter how he chooses to act from here on,\x01",
            "he will have his uses, to be certain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1C,
        (
            "#1884F#5P...You would say that, given that you think of \x01",
            "everyone as your pawns.\x02\x03",

            "#1882FThere's me, the prince, that society...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1B,
        (
            "#1480F#5PIndeed. And I am much the same.\x02\x03",

            "#1485FWe are but pawns on the vast game board that\x01",
            "is the Empire, where a thrill like no other will\x01",
            "take place.\x02\x03",

            "#1481FBut it's because you, too, wish to see how that\x01",
            "game plays out that you've chosen to stand with\x01",
            "me, is it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1C,
        (
            "#1885F#5PWell, hey. What can I say?\x02\x03",

            "#1887FJust don't forget that this piece right here \x01",
            "might not be loyal forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x1B,
        (
            "#1485F#5PAnd such a betrayal would be perfectly fine by\x01",
            "me.\x02\x03",

            "#1480FOr did you honestly think I'd never considered\x01",
            "the possibility it may happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1C,
        (
            "#1884F#5PJust thought I'd come out and say it.\x02\x03",

            "#1880FHow're the other Ironbloods doing, by the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1B,
        (
            "#1481F#5PThey're all doing very well, by the sound of it.\x02\x03",

            "At the rate things are going, there's a chance \x01",
            "all of the prince's efforts will be for naught.\x02\x03",

            "#1485FPerhaps I ought to hold back on him a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1C,
        "#1884F#5PUgh. You sure don't pull any punches, do you?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x1C, 90, 400)
    SetChrSubChip(0x1C, 0)
    Sleep(300)

    ChrTalk(    #32
        0x1C,
        (
            "#1883F#11P...You know something?\x02\x03",

            "#1886FI wouldn't write him off so easily if I were\x01",
            "in your shoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1B,
        "#1482F#5PWhat...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x1B, 90, 400)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x19, 0x1)
    ClearChrFlags(0x1A, 0x1)
    SetChrBattleFlags(0x19, 0x20)
    SetChrBattleFlags(0x1A, 0x20)
    OP_48()
    OP_89(0x19, 184420, -27640, 6520, 180)
    OP_89(0x1A, 183780, -27560, 7620, 180)
    OP_43(0x1A, 0x3, 0x0, 0x1E)
    OP_43(0x10, 0x3, 0x0, 0x1C)
    Sleep(3000)

    def lambda_351F():
        OP_D1(254, 0, 270000, 4000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_351F)
    Sleep(7000)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34 op#A
        0x1B,
        "#1483F#11P#3S#10AWhat?!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x10, 0x3)
    Fade(1000)
    OP_6D(-68320, 16440, -2720, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()
    Sleep(300)
    Fade(1000)
    OP_8C(0x19, 225, 0)
    SetChrChipByIndex(0x19, 7)
    SetChrSubChip(0x19, 3)

    def lambda_35F8():
        OP_99(0xFE, 0x3, 0xC, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_35F8)
    WaitChrThread(0x19, 0x2)
    Sleep(300)

    ChrTalk(    #35 op#A
        0x19,
        "#1545F#5P#10AHeh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x19, 13)
    Sleep(100)
    OP_8C(0x19, 180, 0)
    Sleep(100)

    def lambda_3641():
        OP_99(0xFE, 0xE, 0xF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3641)
    WaitChrThread(0x19, 0x2)

    def lambda_3656():
        OP_6D(-68150, 17300, -6670, 1500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3656)

    def lambda_366E():
        OP_67(0, 3550, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_366E)

    def lambda_3686():
        OP_6C(23000, 1500)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3686)

    def lambda_3696():
        OP_6B(1850, 1500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_3696)

    def lambda_36A6():
        OP_6E(556, 1500)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_36A6)

    def lambda_36B6():
        OP_D0(11000, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_36B6)
    OP_22(0x23B, 0x0, 0x64)
    SetChrPos(0x1F, -69900, 17300, -14320, 0)
    PlayEffect(0x0, 0x0, 0x19, 500, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1F, 0, 0, 0, 0)
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    Sleep(800)

    def lambda_3720():
        OP_99(0xFE, 0x0, 0x4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3720)
    WaitChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 8)
    SetChrSubChip(0x19, 0)
    Sleep(300)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x19, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_377E():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_377E)
    PlayEffect(0x5, 0x3, 0xFF, -69500, 21500, -13660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x19, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_6D(-69700, 17200, -17200, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()

    def lambda_381C():
        OP_67(0, 8500, -10000, 40000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_381C)

    def lambda_3834():
        OP_6B(6000, 40000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3834)
    OP_43(0x1B, 0x3, 0x0, 0x20)
    OP_43(0x1C, 0x3, 0x0, 0x1F)
    WaitChrThread(0x1B, 0x3)
    Sleep(500)

    ChrTalk(    #36 op#A
        0x1B,
        "#1483F#5P#15AThese look like...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0x3)
    Sleep(500)

    ChrTalk(    #37 op#A
        0x1C,
        "#1883F#11P#35ARose petals...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #38 op#A
        (
            "\x07\x05#100AIf you look out the windows on the right-hand\x01",
            "side of the airship, you will be able to see the\x01",
            "famous high-speed cruiser, the Arseille.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #39 op#A op#5
        (
            "\x07\x05#95AWe've been informed that it is on its way to\x01",
            "the Imperial capital with Prince Olivert of the\x01",
            "Erebonian Empire on board...\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #40 op#A
        (
            "\x07\x05#65A...but he has also given us a message to relay\x01",
            "to all of the passengers on board today.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #41 op#A
        (
            "\x07\x05#55A'I give thanks to Aidios for the good fortune to\x01",
            "have been able to meet you today.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #42 op#A
        (
            "\x07\x05#50A'May your journey be filled with beautiful roses\x01",
            "and Her blessings...'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #43 op#A
        (
            "\x07\x05#55A'And, of course, may your journey to your homes\x01",
            "be a safe and pleasant one.'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #44 op#A
        "\x07\x05#10AThat marks the end of his message.\x07\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_44(0x14, 0xFF)
    Fade(1000)
    OP_6D(-68320, 16440, -2720, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D0(0, 0)
    OP_0D()
    PlayEffect(0x1, 0x1, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xFF, -70140, 17200, -18260, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(300)
    SetChrChipByIndex(0x19, 6)
    SetChrSubChip(0x19, 2)
    OP_0D()

    def lambda_3D4E():
        OP_99(0xFE, 0x2, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3D4E)
    WaitChrThread(0x19, 0x2)
    Sleep(500)

    def lambda_3D68():
        OP_6D(-76510, 17200, -5270, 9000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3D68)

    def lambda_3D80():
        OP_67(0, 3680, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3D80)

    def lambda_3D98():
        OP_6C(303000, 9000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3D98)

    def lambda_3DA8():
        OP_6B(3020, 9000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_3DA8)

    def lambda_3DB8():
        OP_6E(686, 9000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_3DB8)
    OP_43(0x19, 0x3, 0x0, 0x1D)

    def lambda_3DCF():
        OP_D1(254, 0, 310000, -14000, 15000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3DCF)

    def lambda_3DE9():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3DE9)
    Sleep(300)

    def lambda_3E09():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E09)
    Sleep(400)

    def lambda_3E29():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E29)
    Sleep(500)

    def lambda_3E49():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E49)
    Sleep(600)

    def lambda_3E69():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E69)
    Sleep(700)

    def lambda_3E89():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E89)
    Sleep(800)

    def lambda_3EA9():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EA9)
    Sleep(900)

    def lambda_3EC9():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EC9)
    Sleep(1000)

    def lambda_3EE9():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EE9)
    Sleep(1000)

    def lambda_3F09():
        OP_8F(0xFE, 0xFFFB57C6, 0x36B0, 0x1F72A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F09)
    WaitChrThread(0x19, 0x3)
    Fade(1000)
    OP_6D(-71580, 17200, -16360, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_8C(0x1B, 270, 0)
    OP_8C(0x1C, 270, 0)
    OP_62(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x1B)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #45
        0x1B,
        "#1484F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x1C,
        (
            "#1883F#6PI never thought there was a bigger dumbass\x01",
            "in this world than me...and yet here we are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1B,
        "#1481F#5PHahaha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #48
        0x1B,
        "#1486F#5P#4SHahahahaha!#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-69380, 17200, -15640, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(110000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0x1B,
        "#1481F#5P#3SVery well, debaucherous prince!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x1B,
        (
            "#1485F#5PI look forward to seeing what you can do!\x02\x03",

            "#1481FShow me how long you can hold out against me!\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)

    def lambda_417D():
        OP_6E(562, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_417D)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_24(0x1C3, 0x5A)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x79, 0xA)
    OP_23(0x1C3)
    OP_23(0x79)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x8, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #51
        "\x07\x00Side Story [Return to the Empire] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D3")
    Sleep(1000)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x4, 0x20)
    OP_3E(0x2ED, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05Received \x1F\xED\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(7000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #53
        "\x07\x05Received \x07\x027,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_42D3")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M7204   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_2CBB end

    def Function_27_42E0(): pass

    label("Function_27_42E0")

    PlayEffect(0x4, 0x2, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2500)
    Sleep(3000)

    label("loc_431A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439A")
    PlayEffect(0x4, 0x1, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1500)
    Sleep(4000)
    PlayEffect(0x4, 0x2, 0xFF, -70900, 21200, -16640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1500)
    Sleep(4000)
    Jump("loc_431A")

    label("loc_439A")

    Return()

    # Function_27_42E0 end

    def Function_28_439B(): pass

    label("Function_28_439B")


    def lambda_43A1():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_43A1)
    Sleep(6000)

    def lambda_43C1():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_43C1)
    Sleep(1000)

    def lambda_43E1():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_43E1)
    Sleep(900)

    def lambda_4401():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4401)
    Sleep(800)

    def lambda_4421():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4421)
    Sleep(700)

    def lambda_4441():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4441)
    Sleep(600)

    def lambda_4461():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4461)
    Sleep(500)

    def lambda_4481():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4481)
    Sleep(400)

    def lambda_44A1():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_44A1)
    Sleep(300)

    def lambda_44C1():
        OP_8F(0xFE, 0xFFFF2856, 0x36B0, 0xFFFFFB5A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_44C1)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_28_439B end

    def Function_29_44DC(): pass

    label("Function_29_44DC")

    OP_24(0x125, 0x46)
    Sleep(2000)
    OP_24(0x125, 0x3C)
    Sleep(2000)
    OP_24(0x125, 0x32)
    Sleep(2000)
    OP_24(0x125, 0x28)
    Sleep(2000)
    OP_24(0x125, 0x1E)
    Sleep(2000)
    OP_24(0x125, 0x14)
    Sleep(2000)
    OP_23(0x125)
    Sleep(1000)
    Return()

    # Function_29_44DC end

    def Function_30_451B(): pass

    label("Function_30_451B")

    Fade(1000)
    OP_6D(110380, 1230, -17180, 0)
    OP_67(0, 3140, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(316000, 0)
    OP_6E(696, 0)
    OP_D0(9000, 0)
    OP_22(0x125, 0x1, 0x46)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 102000, -10000, 640, 270, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 87000, -10000, 640, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x1C, 0, 0)
    OP_8C(0x1B, 0, 0)

    def lambda_45F3():
        OP_6D(-68760, 17300, -8820, 7000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_45F3)

    def lambda_460B():
        OP_67(0, 3140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_460B)

    def lambda_4623():
        OP_6C(86000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_4623)

    def lambda_4633():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_4633)

    def lambda_4643():
        OP_6E(696, 7000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_4643)

    def lambda_4653():
        OP_D0(-9000, 7000)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_4653)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 72000, -10000, 640, 270, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_30_451B end

    def Function_31_4698(): pass

    label("Function_31_4698")

    Sleep(100)
    OP_8C(0x1C, 45, 600)
    Sleep(600)
    OP_8C(0x1C, 0, 600)
    Sleep(700)
    OP_8C(0x1C, 45, 600)
    Sleep(600)
    OP_8C(0x1C, 0, 600)
    Sleep(300)
    Return()

    # Function_31_4698 end

    def Function_32_46CE(): pass

    label("Function_32_46CE")

    OP_8C(0x1B, 270, 600)
    Sleep(800)
    OP_8C(0x1B, 80, 600)
    Sleep(800)
    OP_8C(0x1B, 0, 600)
    Sleep(300)
    Return()

    # Function_32_46CE end

    def Function_33_46F3(): pass

    label("Function_33_46F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, -75000, 30000, -18700, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 271000, 0, 0)
    OP_E5(0x0, 0x0, 0x0, 262144)
    OP_E5(0x0, 0x0, 0x1, 262144)
    OP_E5(0x0, 0x0, 0x2, 262144)
    OP_E5(0x0, 0x0, 0x3, 262144)
    OP_E5(0x0, 0x0, 0x4, 262144)
    OP_E5(0x0, 0x0, 0x5, 262144)
    OP_E5(0x0, 0x0, 0x6, 262144)
    OP_E5(0x0, 0x0, 0x7, 262144)
    OP_E5(0x0, 0x0, 0x8, 262144)
    OP_E5(0x0, 0x0, 0x9, 262144)
    OP_E5(0x0, 0x0, 0xA, 262144)
    OP_E5(0x0, 0x0, 0xB, 262144)
    OP_E5(0x0, 0x0, 0xC, 262144)
    OP_E5(0x0, 0x0, 0xD, 262144)
    OP_E5(0x0, 0x0, 0xE, 262144)
    OP_E5(0x0, 0x0, 0xF, 262144)
    OP_E5(0x0, 0x0, 0x10, 262144)
    OP_E5(0x0, 0x0, 0x11, 262144)
    OP_E5(0x0, 0x0, 0x13, 262144)
    OP_E5(0x0, 0x0, 0x14, 262144)
    OP_E5(0x0, 0x0, 0x15, 262144)
    OP_E5(0x0, 0x0, 0x16, 262144)
    OP_E5(0x0, 0x0, 0x17, 262144)
    OP_E5(0x0, 0x0, 0x18, 262144)
    OP_E5(0x0, 0x0, 0x19, 262144)
    OP_E5(0x0, 0x0, 0x1A, 262144)
    OP_E5(0x0, 0x0, 0x1B, 262144)
    OP_E5(0x0, 0x0, 0x1C, 262144)
    OP_E5(0x0, 0x0, 0x1D, 262144)
    OP_E5(0x0, 0x0, 0x1E, 262144)
    OP_E5(0x2, 0x0, 0x0, 200)
    OP_E5(0x2, 0x0, 0x1, 200)
    OP_E5(0x2, 0x0, 0x2, 200)
    OP_E5(0x2, 0x0, 0x3, 200)
    OP_E5(0x2, 0x0, 0x4, 200)
    OP_E5(0x2, 0x0, 0x5, 200)
    OP_E5(0x2, 0x0, 0x6, 200)
    OP_E5(0x2, 0x0, 0x7, 200)
    OP_E5(0x2, 0x0, 0x8, 200)
    OP_E5(0x2, 0x0, 0x9, 200)
    OP_E5(0x2, 0x0, 0xA, 200)
    OP_E5(0x2, 0x0, 0xB, 200)
    OP_E5(0x2, 0x0, 0xC, 200)
    OP_E5(0x2, 0x0, 0xD, 200)
    OP_E5(0x2, 0x0, 0xE, 200)
    OP_E5(0x2, 0x0, 0xF, 200)
    OP_E5(0x2, 0x0, 0x10, 200)
    OP_E5(0x2, 0x0, 0x11, 200)
    OP_E5(0x2, 0x0, 0x13, 200)
    OP_E5(0x2, 0x0, 0x14, 200)
    OP_E5(0x2, 0x0, 0x15, 200)
    OP_E5(0x2, 0x0, 0x16, 200)
    OP_E5(0x2, 0x0, 0x17, 200)
    OP_E5(0x2, 0x0, 0x18, 200)
    OP_E5(0x2, 0x0, 0x19, 200)
    OP_E5(0x2, 0x0, 0x1A, 200)
    OP_E5(0x2, 0x0, 0x1B, 200)
    OP_E5(0x2, 0x0, 0x1C, 200)
    OP_E5(0x2, 0x0, 0x1D, 200)
    OP_E5(0x2, 0x0, 0x1E, 200)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x3C)
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFB0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFD8, 0xFFFFFFF6, 0x0, 0x0, 0x0)

    def lambda_4A56():

        label("loc_4A56")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_4A56")

    QueueWorkItem2(0x10, 2, lambda_4A56)
    OP_22(0x1C3, 0x0, 0x64)
    Sleep(3000)
    OP_6D(-200850, 45000, 4180, 0)
    OP_67(0, -2340, -10000, 0)
    OP_6B(6500, 0)
    OP_6C(10000, 0)
    OP_6E(748, 0)
    FadeToBright(2000, 0)

    def lambda_4AC1():
        OP_6D(-140000, 9000, 1500, 8000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4AC1)

    def lambda_4AD9():
        OP_67(0, 8500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4AD9)

    def lambda_4AF1():
        OP_6B(7380, 8000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_4AF1)

    def lambda_4B01():
        OP_6C(30000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_4B01)

    def lambda_4B11():
        OP_6E(848, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_4B11)

    def lambda_4B21():
        OP_D0(-3000, 8000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4B21)
    WaitChrThread(0x20, 0x0)
    OP_43(0x10, 0x3, 0x0, 0x22)

    def lambda_4B3D():
        OP_6D(-57500, 9000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4B3D)

    def lambda_4B55():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_4B55)
    WaitChrThread(0x20, 0x0)

    def lambda_4B6A():
        OP_6B(6300, 15000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4B6A)

    def lambda_4B7A():
        OP_6E(760, 15000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_4B7A)
    Sleep(1000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x69, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS542._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(4000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_43(0x10, 0x3, 0x0, 0x23)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_46F3 end

    def Function_34_4BFC(): pass

    label("Function_34_4BFC")

    OP_22(0x2D5, 0x1, 0x0)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x32)
    Sleep(200)
    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x3C)
    Sleep(200)
    OP_24(0x2D5, 0x46)
    Sleep(200)
    OP_24(0x2D5, 0x50)
    Sleep(200)
    OP_24(0x2D5, 0x5A)
    Sleep(200)
    OP_24(0x2D5, 0x64)
    Return()

    # Function_34_4BFC end

    def Function_35_4C65(): pass

    label("Function_35_4C65")

    OP_24(0x1C3, 0x5A)
    OP_24(0x2D5, 0x5A)
    Sleep(300)
    OP_24(0x1C3, 0x50)
    OP_24(0x2D5, 0x50)
    Sleep(300)
    OP_24(0x1C3, 0x46)
    OP_24(0x2D5, 0x46)
    Sleep(300)
    OP_24(0x1C3, 0x3C)
    OP_24(0x2D5, 0x3C)
    Sleep(300)
    OP_24(0x1C3, 0x32)
    OP_24(0x2D5, 0x32)
    Sleep(300)
    OP_24(0x1C3, 0x28)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    OP_23(0x1C3)
    OP_23(0x2D5)
    Return()

    # Function_35_4C65 end

    def Function_36_4CE9(): pass

    label("Function_36_4CE9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_72(0x400, 0x0)
    ExitThread()
    OP_A1(0x10, 0x0)
    SetChrPos(0x10, 220000, 30000, -18700, 0)
    ClearChrFlags(0x10, 0x100)
    OP_8C(0x10, 0, 0)
    OP_D1(16, 0, 271000, 0, 0)
    OP_E5(0x0, 0x0, 0x0, 262144)
    OP_E5(0x0, 0x0, 0x1, 262144)
    OP_E5(0x0, 0x0, 0x2, 262144)
    OP_E5(0x0, 0x0, 0x3, 262144)
    OP_E5(0x0, 0x0, 0x4, 262144)
    OP_E5(0x0, 0x0, 0x5, 262144)
    OP_E5(0x0, 0x0, 0x6, 262144)
    OP_E5(0x0, 0x0, 0x7, 262144)
    OP_E5(0x0, 0x0, 0x8, 262144)
    OP_E5(0x0, 0x0, 0x9, 262144)
    OP_E5(0x0, 0x0, 0xA, 262144)
    OP_E5(0x0, 0x0, 0xB, 262144)
    OP_E5(0x0, 0x0, 0xC, 262144)
    OP_E5(0x0, 0x0, 0xD, 262144)
    OP_E5(0x0, 0x0, 0xE, 262144)
    OP_E5(0x0, 0x0, 0xF, 262144)
    OP_E5(0x0, 0x0, 0x10, 262144)
    OP_E5(0x0, 0x0, 0x11, 262144)
    OP_E5(0x0, 0x0, 0x13, 262144)
    OP_E5(0x0, 0x0, 0x14, 262144)
    OP_E5(0x0, 0x0, 0x15, 262144)
    OP_E5(0x0, 0x0, 0x16, 262144)
    OP_E5(0x0, 0x0, 0x17, 262144)
    OP_E5(0x0, 0x0, 0x18, 262144)
    OP_E5(0x0, 0x0, 0x19, 262144)
    OP_E5(0x0, 0x0, 0x1A, 262144)
    OP_E5(0x0, 0x0, 0x1B, 262144)
    OP_E5(0x0, 0x0, 0x1C, 262144)
    OP_E5(0x0, 0x0, 0x1D, 262144)
    OP_E5(0x0, 0x0, 0x1E, 262144)
    OP_E5(0x2, 0x0, 0x0, 200)
    OP_E5(0x2, 0x0, 0x1, 200)
    OP_E5(0x2, 0x0, 0x2, 200)
    OP_E5(0x2, 0x0, 0x3, 200)
    OP_E5(0x2, 0x0, 0x4, 200)
    OP_E5(0x2, 0x0, 0x5, 200)
    OP_E5(0x2, 0x0, 0x6, 200)
    OP_E5(0x2, 0x0, 0x7, 200)
    OP_E5(0x2, 0x0, 0x8, 200)
    OP_E5(0x2, 0x0, 0x9, 200)
    OP_E5(0x2, 0x0, 0xA, 200)
    OP_E5(0x2, 0x0, 0xB, 200)
    OP_E5(0x2, 0x0, 0xC, 200)
    OP_E5(0x2, 0x0, 0xD, 200)
    OP_E5(0x2, 0x0, 0xE, 200)
    OP_E5(0x2, 0x0, 0xF, 200)
    OP_E5(0x2, 0x0, 0x10, 200)
    OP_E5(0x2, 0x0, 0x11, 200)
    OP_E5(0x2, 0x0, 0x13, 200)
    OP_E5(0x2, 0x0, 0x14, 200)
    OP_E5(0x2, 0x0, 0x15, 200)
    OP_E5(0x2, 0x0, 0x16, 200)
    OP_E5(0x2, 0x0, 0x17, 200)
    OP_E5(0x2, 0x0, 0x18, 200)
    OP_E5(0x2, 0x0, 0x19, 200)
    OP_E5(0x2, 0x0, 0x1A, 200)
    OP_E5(0x2, 0x0, 0x1B, 200)
    OP_E5(0x2, 0x0, 0x1C, 200)
    OP_E5(0x2, 0x0, 0x1D, 200)
    OP_E5(0x2, 0x0, 0x1E, 200)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x3C)
    LoadEffect(0x2, "map\\mp096_00.eff")
    LoadEffect(0x0, "map\\mp201_01.eff")
    PlayEffect(0x0, 0xFF, 0x10, 0, 0, 13000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, 4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x10, -4300, 1800, 10000, 90, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_48()
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFB0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFD8, 0xFFFFFFF6, 0x0, 0x0, 0x0)

    def lambda_505F():

        label("loc_505F")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_505F")

    QueueWorkItem2(0x10, 2, lambda_505F)
    OP_22(0x1C3, 0x0, 0x64)
    OP_6D(94640, 37400, -25730, 0)
    OP_67(0, -2910, -10000, 0)
    OP_6B(9310, 0)
    OP_6C(278000, 0)
    OP_6E(600, 0)

    def lambda_50BC():
        OP_6D(93740, 41000, -19000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_50BC)

    def lambda_50D4():
        OP_67(0, -50, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_50D4)

    def lambda_50EC():
        OP_6B(14000, 15000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_50EC)

    def lambda_50FC():
        OP_6C(270000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_50FC)

    def lambda_510C():
        OP_6E(800, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_510C)
    StopSound(0x4E20, 0x927C0, 0x32C8)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayEffect(0x2, 0xFF, 0xFF, 135000, 40000, -20700, 40, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_43(0x10, 0x3, 0x0, 0x27)
    OP_43(0x10, 0x0, 0x0, 0x25)
    Sleep(1000)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0x26)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #54 op#A op#5
        (
            "\x07\x0C#40AUnless you want to live the rest of your life\x01",
            "in abject shame...\x02\x03\x05",

            "#40A...then for the love of Aidios, get Ries to help\x01",
            "you choose. Don't even think of picking alone.\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    WaitChrThread(0x10, 0x3)
    Sleep(3000)
    OP_1D(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0x0, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS477._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x96, 0x78, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS478._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x7, 0, -320000, 7000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(3000)
    OP_56(0x2)
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    OP_A2(0x2C27)
    OP_A2(0x2582)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2502)
    OP_F7(0x8, 0x0, 0x0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05Save Clear Data?\x18\x02",
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53AC")
    OP_DC(0x0, 0x3)
    ShowSaveMenu()
    EventBegin(0x4)

    label("loc_53AC")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    FadeToDark(0, 0, -1)
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_36_4CE9 end

    def Function_37_53D8(): pass

    label("Function_37_53D8")


    def lambda_53DE():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_53DE)
    Sleep(500)

    def lambda_53FE():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_53FE)
    Sleep(500)

    def lambda_541E():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_541E)
    Sleep(3500)

    def lambda_543E():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_543E)
    Sleep(2500)

    def lambda_545E():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_545E)
    Sleep(1500)

    def lambda_547E():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_547E)
    Sleep(1000)

    def lambda_549E():
        OP_91(0xFE, 0xFFF85EE0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_549E)
    Sleep(500)
    Return()

    # Function_37_53D8 end

    def Function_38_54B9(): pass

    label("Function_38_54B9")

    Sleep(5000)
    OP_24(0x1C3, 0x5A)
    OP_24(0x2D5, 0x5A)
    Sleep(1000)
    OP_24(0x1C3, 0x50)
    OP_24(0x2D5, 0x50)
    Sleep(1000)
    OP_24(0x1C3, 0x46)
    OP_24(0x2D5, 0x46)
    Sleep(1000)
    OP_24(0x1C3, 0x3C)
    OP_24(0x2D5, 0x3C)
    Sleep(1000)
    OP_24(0x1C3, 0x32)
    OP_24(0x2D5, 0x32)
    Sleep(1000)
    OP_24(0x1C3, 0x28)
    OP_24(0x2D5, 0x28)
    Sleep(1000)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(1000)
    OP_24(0x1C3, 0x1E)
    OP_24(0x2D5, 0x1E)
    Sleep(1000)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    Sleep(1000)
    OP_24(0x1C3, 0xA)
    OP_24(0x2D5, 0xA)
    OP_23(0x1C3)
    OP_23(0x2D5)
    Return()

    # Function_38_54B9 end

    def Function_39_5542(): pass

    label("Function_39_5542")

    OP_22(0x2D5, 0x1, 0x0)
    Sleep(100)
    OP_24(0x2D5, 0xA)
    Sleep(100)
    OP_24(0x2D5, 0x14)
    Sleep(100)
    OP_24(0x2D5, 0x1E)
    Sleep(100)
    OP_24(0x2D5, 0x28)
    Sleep(100)
    OP_24(0x2D5, 0x32)
    Sleep(100)
    OP_24(0x2D5, 0x46)
    Sleep(100)
    OP_24(0x2D5, 0x3C)
    Sleep(100)
    OP_24(0x2D5, 0x46)
    Sleep(100)
    OP_24(0x2D5, 0x50)
    Sleep(100)
    OP_24(0x2D5, 0x5A)
    Sleep(100)
    OP_24(0x2D5, 0x64)
    Return()

    # Function_39_5542 end

    SaveToFile()

Try(main)
