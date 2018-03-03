from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Mirano',                               # 9
        'Kanone',                               # 10
        'Mayor Norman',                         # 11
        'Boat',                                 # 12
        'Target Camera',                        # 13
        'Hardt',                                # 14
        'Harg',                                 # 15
        'Brenda',                               # 16
        'Aurian Causeway',                      # 17
        'Ruan - North Block',                   # 18
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
        'ED6_DT07/CH01760 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01110 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH00472 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01080 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH01680 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01190 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01390 ._CH',             # 14
        'ED6_DT07/CH02530 ._CH',             # 15
        'ED6_DT07/CH01230 ._CH',             # 16
        'ED6_DT26/CH20797 ._CH',             # 17
        'ED6_DT07/CH01200 ._CH',             # 18
    )

    AddCharChipPat(
        'ED6_DT07/CH01760P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01110P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH00472P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01080P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH01680P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01190P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01390P._CP',             # 14
        'ED6_DT07/CH02530P._CP',             # 15
        'ED6_DT07/CH01230P._CP',             # 16
        'ED6_DT26/CH20797P._CP',             # 17
        'ED6_DT07/CH01200P._CP',             # 18
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0xA0,
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
        X                   = 30790,
        Z                   = 0,
        Y                   = 9980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 35750,
        Z                   = 0,
        Y                   = 25180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75930,
        Z                   = 0,
        Y                   = 10740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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

    DeclNpc(
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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


    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_35E",          # 00, 0
        "Function_1_3BF",          # 01, 1
        "Function_2_47B",          # 02, 2
        "Function_3_5F8",          # 03, 3
        "Function_4_618",          # 04, 4
        "Function_5_63C",          # 05, 5
        "Function_6_837",          # 06, 6
        "Function_7_F26",          # 07, 7
        "Function_8_F80",          # 08, 8
        "Function_9_1402",         # 09, 9
        "Function_10_1463",        # 0A, 10
        "Function_11_14B2",        # 0B, 11
        "Function_12_14B9",        # 0C, 12
        "Function_13_14BD",        # 0D, 13
    )


    def Function_0_35E(): pass

    label("Function_0_35E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_38C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_A2(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_3BE")

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_3AB")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_3BE")

    label("loc_3AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3BE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_3BE")

    Return()

    # Function_0_35E end

    def Function_1_3BF(): pass

    label("Function_1_3BF")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F8")
    OP_A3(0x0)
    OP_B1("T2101_1")
    Jump("loc_401")

    label("loc_3F8")

    OP_B1("T2101_0")

    label("loc_401")

    OP_72(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 60)
    OP_72(0x1012, 0x0)
    ExitThread()
    OP_72(0x1014, 0x0)
    ExitThread()
    OP_72(0x1015, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x422, 0x0)
    ExitThread()
    OP_64(0x3, 0x1)
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_1C(0x13, 0x0, 0xB)
    OP_82(0x87, 0x0)
    Return()

    # Function_1_3BF end

    def Function_2_47B(): pass

    label("Function_2_47B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5E2")

    label("loc_4A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B9")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5E2")

    label("loc_4B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5E2")

    label("loc_4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5E2")

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5E2")

    label("loc_504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5E2")

    label("loc_51D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5E2")

    label("loc_536")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5E2")

    label("loc_54F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_568")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5E2")

    label("loc_568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5E2")

    label("loc_581")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5E2")

    label("loc_59A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5E2")

    label("loc_5B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5E2")

    label("loc_5CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5E2")

    label("loc_5F7")

    Return()

    # Function_2_47B end

    def Function_3_5F8(): pass

    label("Function_3_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x1, 0x7, 0xBB8)
    SetChrSubChip(0xFE, 0)
    Sleep(250)
    Jump("Function_3_5F8")

    label("loc_617")

    Return()

    # Function_3_5F8 end

    def Function_4_618(): pass

    label("Function_4_618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63B")
    OP_8D(0xFE, 48840, 21930, 53280, 24890, 2000)
    Jump("Function_4_618")

    label("loc_63B")

    Return()

    # Function_4_618 end

    def Function_5_63C(): pass

    label("Function_5_63C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 79860, 4000, -920, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, 83000, 3500, -920, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, 45750, 0, 25250, 0)
    SetChrPos(0x16, 73700, 0, 21410, 270)

    def lambda_6B1():
        OP_8F(0xFE, 0x68CE, 0x0, 0x53A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6B1)
    OP_6D(51000, 0, 33880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(600, 0)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x7D0)

    def lambda_727():
        OP_6D(80560, 0, 2360, 14000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_727)

    def lambda_73F():
        OP_67(0, 6540, -10000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_73F)

    def lambda_757():
        OP_6C(135000, 14000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_757)

    def lambda_767():
        OP_6E(384, 14000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_767)
    WaitChrThread(0x14, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05R&A Research - Ruan Office\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    ChrTalk(    #1
        0x10,
        "#4POh, my... Look at all of this.\x02",
    )

    CloseMessageWindow()
    SetPlaceName(0x69)

    NpcTalk(    #2
        0x10C,
        "Director",
        "#3PI hope it will prove useful.\x02",
    )

    CloseMessageWindow()

    def lambda_815():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_815)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2110   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_5_63C end

    def Function_6_837(): pass

    label("Function_6_837")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(79240, 0, 6460, 0)
    OP_67(0, 9040, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(404, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10C, 79240, 500, 5000, 270)
    SetChrPos(0x11, 79240, 500, 5000, 270)
    SetChrPos(0x12, 79240, 500, 5000, 270)
    OP_9F(0x10C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8E4():
        OP_67(0, 6540, -10000, 7200)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8E4)
    FadeToBright(2000, 0)
    OP_0D()
    OP_72(0x100F, 0x0)
    ExitThread()
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    Sleep(100)

    def lambda_91B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_91B)

    def lambda_92D():
        OP_8E(0xFE, 0x123B8, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_92D)
    Sleep(700)
    OP_43(0x11, 0x3, 0x0, 0x7)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 90, 400)

    def lambda_960():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_960)

    def lambda_972():
        OP_8E(0xFE, 0x1291C, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_972)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    Fade(1000)
    OP_44(0x14, 0x0)
    OP_6D(75500, 0, 5080, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_6D(76280, 0, 5360, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10C)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_8C(0x12, 0, 400)

    def lambda_A75():

        label("loc_A75")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_A75")

    QueueWorkItem2(0x10C, 2, lambda_A75)

    def lambda_A86():

        label("loc_A86")

        TurnDirection(0xFE, 0x12, 0)
        OP_48()
        Jump("loc_A86")

    QueueWorkItem2(0x11, 2, lambda_A86)

    def lambda_A97():
        OP_6D(76090, 0, 6470, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_A97)

    def lambda_AAF():
        OP_8E(0xFE, 0x1291C, 0x0, 0x445C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AAF)
    WaitChrThread(0x12, 0x1)

    def lambda_ACF():
        OP_6D(75890, 0, 5130, 2000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_ACF)
    OP_44(0x10C, 0x2)
    OP_44(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    Sleep(500)

    NpcTalk(    #3
        0x10C,
        "Richard",
        (
            "#1850F#5PAll seems to be going rather well with\x01",
            "this business now, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#1862F#12PIndeed...\x02\x03",

            "#1861FAlthough, I admit that it's taking me time\x01",
            "to adjust my days being so...peaceful. I do\x01",
            "miss having a sense of tension in my life.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x11, 400)
    Sleep(300)

    NpcTalk(    #5
        0x10C,
        "Richard",
        (
            "#1851F#5PThat's something you'll just have to\x01",
            "live with, I'm afraid. We're civilians\x01",
            "now. Not soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#1861F#12P...That's true enough.\x02\x03",

            "#1862FIn any case, it's an honor to be able to \x01",
            "live and work with you in the city where\x01",
            "you were born, Your Excellency.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10C,
        "Richard",
        (
            "#1855F#5P...Kanone.\x02\x03",

            "#1850FI really would prefer it if you addressed\x01",
            "me as 'sir' now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        "#1864F#12P...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #9
        0x11,
        "#1861F#12PM-My apologies, sir!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x10C,
        "Richard",
        "#1851F#5PHaha. There's no need to apologize.\x02",
    )

    CloseMessageWindow()
    OP_22(0x168, 0x0, 0x64)
    OP_77(0xA0, 0xA0, 0xA0, 0x0, 0x7D0)
    Sleep(2500)
    OP_8C(0x10C, 270, 400)
    Sleep(500)

    NpcTalk(    #11
        0x10C,
        "Richard",
        (
            "#1850F#5PWell, I think we should probably go inside.\x01",
            "I'm not sure I like the look of the sky.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_E98():

        label("loc_E98")

        TurnDirection(0xFE, 0x10C, 500)
        OP_48()
        Jump("loc_E98")

    QueueWorkItem2(0x11, 2, lambda_E98)
    OP_8C(0x10C, 90, 500)

    def lambda_EB0():
        OP_8E(0xFE, 0x13588, 0x1F4, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_EB0)
    Sleep(500)
    OP_44(0x11, 0x2)

    def lambda_ED4():
        OP_8E(0xFE, 0x12804, 0x0, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_ED4)
    WaitChrThread(0x11, 0x1)

    def lambda_EF4():
        OP_8E(0xFE, 0x13588, 0x1F4, 0x1388, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_EF4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2110   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_6_837 end

    def Function_7_F26(): pass

    label("Function_7_F26")


    def lambda_F2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_F2C)

    def lambda_F3E():
        OP_8E(0xFE, 0x12804, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F3E)
    WaitChrThread(0x11, 0x1)

    def lambda_F5E():
        OP_8E(0xFE, 0x123B8, 0x0, 0xF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_F5E)
    WaitChrThread(0x11, 0x1)
    OP_8C(0x11, 45, 400)
    Return()

    # Function_7_F26 end

    def Function_8_F80(): pass

    label("Function_8_F80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    SoundLoad(457)
    OP_11(0x0, 0x0, 0x0, 0x80E8, 0x1FBD0, 0x0)
    OP_6D(72140, 0, 23640, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(500, 0)
    SetChrFlags(0x10C, 0x4)
    SetChrPos(0x10C, 72220, 0, 7120, 0)
    OP_43(0x10C, 0x3, 0x0, 0x9)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1600)

    ChrTalk(    #12 op#A
        0x10C,
        "#11P#1855F#25A(Ugh...)\x02",
    )

    Sleep(400)

    def lambda_1042():
        OP_6D(50800, 0, 30160, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1042)

    def lambda_105A():
        OP_6C(320000, 4000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_105A)

    def lambda_106A():
        OP_6E(410, 4000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_106A)
    Sleep(4400)

    ChrTalk(    #13 op#A
        0x10C,
        "#5P#1856F#15A(There's no mistaking it.)\x02",
    )

    WaitChrThread(0x14, 0x0)
    Sleep(2000)
    PlayEffect(0x0, 0xFF, 0xFF, 50800, 0, 30160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x1, 0x1E)
    Sleep(300)
    OP_24(0x1C9, 0x28)
    Sleep(300)
    OP_24(0x1C9, 0x32)
    Sleep(300)
    OP_24(0x1C9, 0x3C)
    Sleep(300)
    OP_24(0x1C9, 0x46)
    Sleep(300)
    OP_24(0x1C9, 0x50)
    Sleep(300)
    OP_24(0x1C9, 0x5A)
    Sleep(300)
    OP_24(0x1C9, 0x64)
    Sleep(3000)
    WaitChrThread(0x10C, 0x3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x18\x07\x0CThat letter was sealed in a special way we used\x01",
            "in the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x18\x07\x0CThe letter itself is a meaningless decoy; the real\x01",
            "message is concealed in how the envelope itself\x01",
            "is sealed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #16
        "\x18\x07\x0CIt means, 'Come to the landing port.'\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x18\x07\x0CSomeone from the Intelligence Division is calling\x01",
            "me in hopes of speaking to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x18\x07\x0CMost likely because they bear a deep-seated\x01",
            "resentment towards me and what I did to them...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x169, 0x0, 0x50)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x18\x07\x0C...and I have a duty to go and see them.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        "\x18\x07\x0CAfter all, I was their commander.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x18\x07\x0CI was the one who pushed their life off the rails\x01",
            "and ruined their future...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_F80 end

    def Function_9_1402(): pass

    label("Function_9_1402")


    def lambda_1408():
        OP_8E(0xFE, 0x11A1C, 0x0, 0x56E0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1408)
    WaitChrThread(0x10C, 0x1)

    def lambda_1428():
        OP_8E(0xFE, 0xCABC, 0x0, 0x57A8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1428)
    WaitChrThread(0x10C, 0x1)

    def lambda_1448():
        OP_8E(0xFE, 0xC738, 0x0, 0xA500, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1448)
    WaitChrThread(0x10C, 0x1)
    Return()

    # Function_9_1402 end

    def Function_10_1463(): pass

    label("Function_10_1463")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_1463 end

    def Function_11_14B2(): pass

    label("Function_11_14B2")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_11_14B2 end

    def Function_12_14B9(): pass

    label("Function_12_14B9")

    SetPlaceName(0x69)
    Return()

    # Function_12_14B9 end

    def Function_13_14BD(): pass

    label("Function_13_14BD")

    SetPlaceName(0x52)
    Return()

    # Function_13_14BD end

    SaveToFile()

Try(main)
