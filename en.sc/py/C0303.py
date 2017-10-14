from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0303   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0303.x',
        MapIndex            = 19,
        MapDefaultBGM       = "ed60021",
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
        'Zaqqum',                               # 9
        'Jubokko ',                             # 10
        'Mirage',                               # 11
        'Mirage',                               # 12
        'Luciola',                              # 13
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
        'ED6_DT29/CH12380 ._CH',             # 00
        'ED6_DT09/CH10910 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT27/CH03004 ._CH',             # 03
        'ED6_DT07/CH00054 ._CH',             # 04
        'ED6_DT07/CH00064 ._CH',             # 05
        'ED6_DT07/CH00034 ._CH',             # 06
        'ED6_DT07/CH00044 ._CH',             # 07
        'ED6_DT07/CH00074 ._CH',             # 08
        'ED6_DT26/CH20235 ._CH',             # 09
        'ED6_DT07/CH00122 ._CH',             # 0A
        'ED6_DT27/CH03520 ._CH',             # 0B
        'ED6_DT27/CH04000 ._CH',             # 0C
        'ED6_DT27/CH04001 ._CH',             # 0D
        'ED6_DT07/CH00150 ._CH',             # 0E
        'ED6_DT07/CH00151 ._CH',             # 0F
        'ED6_DT07/CH00120 ._CH',             # 10
        'ED6_DT07/CH00121 ._CH',             # 11
        'ED6_DT07/CH00160 ._CH',             # 12
        'ED6_DT07/CH00161 ._CH',             # 13
        'ED6_DT07/CH00140 ._CH',             # 14
        'ED6_DT07/CH00141 ._CH',             # 15
        'ED6_DT07/CH00130 ._CH',             # 16
        'ED6_DT07/CH00131 ._CH',             # 17
        'ED6_DT07/CH00170 ._CH',             # 18
        'ED6_DT07/CH00171 ._CH',             # 19
        'ED6_DT29/CH12381 ._CH',             # 1A
        'ED6_DT09/CH10911 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT29/CH12380P._CP',             # 00
        'ED6_DT09/CH10910P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT27/CH03004P._CP',             # 03
        'ED6_DT07/CH00054P._CP',             # 04
        'ED6_DT07/CH00064P._CP',             # 05
        'ED6_DT07/CH00034P._CP',             # 06
        'ED6_DT07/CH00044P._CP',             # 07
        'ED6_DT07/CH00074P._CP',             # 08
        'ED6_DT26/CH20235P._CP',             # 09
        'ED6_DT07/CH00122P._CP',             # 0A
        'ED6_DT27/CH03520P._CP',             # 0B
        'ED6_DT27/CH04000P._CP',             # 0C
        'ED6_DT27/CH04001P._CP',             # 0D
        'ED6_DT07/CH00150P._CP',             # 0E
        'ED6_DT07/CH00151P._CP',             # 0F
        'ED6_DT07/CH00120P._CP',             # 10
        'ED6_DT07/CH00121P._CP',             # 11
        'ED6_DT07/CH00160P._CP',             # 12
        'ED6_DT07/CH00161P._CP',             # 13
        'ED6_DT07/CH00140P._CP',             # 14
        'ED6_DT07/CH00141P._CP',             # 15
        'ED6_DT07/CH00130P._CP',             # 16
        'ED6_DT07/CH00131P._CP',             # 17
        'ED6_DT07/CH00170P._CP',             # 18
        'ED6_DT07/CH00171P._CP',             # 19
        'ED6_DT29/CH12381P._CP',             # 1A
        'ED6_DT09/CH10911P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E5,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -50270,
        Y                   = -1000,
        Z                   = 12650,
        Range               = -44030,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2652,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 53690,
        TriggerZ            = 360,
        TriggerY            = 7930,
        TriggerRange        = 1000,
        ActorX              = 57030,
        ActorZ              = -1000,
        ActorY              = 7730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26E",          # 00, 0
        "Function_1_2B9",          # 01, 1
        "Function_2_508",          # 02, 2
        "Function_3_685",          # 03, 3
        "Function_4_A3A",          # 04, 4
        "Function_5_CDE",          # 05, 5
        "Function_6_1387",         # 06, 6
        "Function_7_1D5B",         # 07, 7
        "Function_8_2232",         # 08, 8
        "Function_9_3F13",         # 09, 9
        "Function_10_3F5F",        # 0A, 10
        "Function_11_4048",        # 0B, 11
        "Function_12_4131",        # 0C, 12
        "Function_13_41DC",        # 0D, 13
        "Function_14_4287",        # 0E, 14
        "Function_15_442B",        # 0F, 15
        "Function_16_44CA",        # 10, 16
    )


    def Function_0_26E(): pass

    label("Function_0_26E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D")
    Event(0, 3)
    Jump("loc_2B8")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_28E")
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_2B8")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2A8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 8)
    Jump("loc_2B8")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B8")
    Event(0, 4)

    label("loc_2B8")

    Return()

    # Function_0_26E end

    def Function_1_2B9(): pass

    label("Function_1_2B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x45F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CE")

    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FB")
    OP_C4(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4FB")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    LoadEffect(0x0, "map\\\\mp073_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -54310, -110, 10630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -51620, -110, 7230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, -49800, -110, 8380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -44290, -110, 8029, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, -40610, -110, 10800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, -40940, 270, 7260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_507")
    OP_64(0x0, 0x1)

    label("loc_507")

    Return()

    # Function_1_2B9 end

    def Function_2_508(): pass

    label("Function_2_508")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_66F")

    label("loc_52D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_66F")

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_66F")

    label("loc_55F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_66F")

    label("loc_578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_66F")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_66F")

    label("loc_5AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_66F")

    label("loc_5C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_66F")

    label("loc_5DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_66F")

    label("loc_5F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_66F")

    label("loc_60E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_66F")

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_66F")

    label("loc_640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_66F")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_66F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_684")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_66F")

    label("loc_684")

    Return()

    # Function_2_508 end

    def Function_3_685(): pass

    label("Function_3_685")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E3")
    SetChrPos(0x101, 49450, -350, -30730, 0)
    SetChrPos(0x103, 50560, -230, -31130, 0)
    SetChrPos(0xF8, 48880, -290, -32340, 0)
    SetChrPos(0xF9, 50160, -270, -32750, 0)
    OP_6D(49950, -200, -24790, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)

    def lambda_720():
        OP_90(0xFE, 0x0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_720)
    Sleep(50)

    def lambda_740():
        OP_90(0xFE, 0x0, 0x0, 0x15E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_740)
    Sleep(200)

    def lambda_760():
        OP_90(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_760)
    Sleep(50)

    def lambda_780():
        OP_90(0xFE, 0x0, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_780)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_11(0xFF, 0xFF, 0xFF, 0x7530, 0xEA60, 0x0)
    SetMapFlags(0x10)
    StopSound(0x258, 0xC544, 0xBB8)
    Sleep(3000)

    ChrTalk(    #0
        0x101,
        (
            "#1000F◆わわっ……\x01",
            "霧が濃くて何も見えない。\x02\x03",

            "◆どうしよう、シェラ姉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#020F◆……仕方ない。\x01",
            "　\x09もと来た道を引き返すわよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_85F)
    Sleep(50)

    def lambda_87F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_87F)
    Sleep(100)

    def lambda_89F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_89F)
    Sleep(50)

    def lambda_8BF():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8BF)
    OP_A2(0x1841)
    NewScene("ED6_DT21/C0301   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_A39")

    label("loc_8E3")

    SetChrPos(0x101, 49500, -250, -24090, 0)
    SetChrPos(0x103, 50640, -140, -24610, 0)
    SetChrPos(0xF8, 49370, -300, -25770, 0)
    SetChrPos(0xF9, 50600, -200, -26310, 0)
    OP_6D(49950, -200, -24790, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x4E20, 0xAFC8, 0x0)
    SetMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #2
        0x103,
        (
            "#020F◆霧ストッパー\x01",
            "　繰り返しメッセージよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9BB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_9BB)
    Sleep(50)

    def lambda_9DB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_9DB)
    Sleep(100)

    def lambda_9FB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9FB)
    Sleep(50)

    def lambda_A1B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A1B)
    NewScene("ED6_DT21/C0301   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_A39")

    Return()

    # Function_3_685 end

    def Function_4_A3A(): pass

    label("Function_4_A3A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5A")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)

    label("loc_A5A")

    SetChrPos(0x101, -49280, -190, -27370, 0)
    SetChrPos(0x103, -50190, -340, -27080, 0)
    SetChrPos(0xF8, -49390, -220, -28460, 0)
    SetChrPos(0xF9, -50350, -340, -28170, 0)
    OP_6D(-49490, -230, -27200, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B49")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B87")

    label("loc_B49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B70")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B87")

    label("loc_B70")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAE")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BEC")

    label("loc_BAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BEC")

    label("loc_BD5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BEC")

    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #3
        0x101,
        "#1020F#5PWaaaah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3A")

    ChrTalk(    #4
        0x108,
        "#072FCrap!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5A")

    ChrTalk(    #5
        0x106,
        "#057FTch!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C79")

    ChrTalk(    #6
        0x104,
        "#033FOh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #7
        0x105,
        "#043FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #8
        0x107,
        "#065FWawawaaa!\x02",
    )

    CloseMessageWindow()

    label("loc_CBA")


    ChrTalk(    #9
        0x103,
        "#523F#6PTsk!\x02",
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0304   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_4_A3A end

    def Function_5_CDE(): pass

    label("Function_5_CDE")

    EventBegin(0x4)
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D08")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)

    label("loc_D08")

    SetChrPos(0x101, -49280, -190, -27370, 0)
    SetChrPos(0x103, -50190, -340, -27080, 0)
    SetChrPos(0xF8, -49390, -220, -28460, 0)
    SetChrPos(0xF9, -50350, -340, -28170, 0)
    OP_6D(-49490, -230, -27200, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x101,
        "#1025F#6PWe're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#022F#6PThis is near the Great Servais Tree.\x02\x03",

            "#026FIt seems we got lost in...an illusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x316, 0)), scpexpr(EXPR_END)), "loc_F47")

    ChrTalk(    #12
        0x101,
        "#1020F#4PAn illusion?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x101,
        (
            "#1005F#4PWait a minute!\x02\x03",

            "That's why we couldn't find the\x01",
            "road to the Great Tree?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    Sleep(500)

    ChrTalk(    #14
        0x103,
        (
            "#524F#6PNoticed it too, did you?\x02\x03",

            "The illusion was disguising it so that\x01",
            "we couldn't see the path farther in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1020F#4PTh-That...\x02",
    )

    CloseMessageWindow()
    Jump("loc_F64")

    label("loc_F47")


    ChrTalk(    #16
        0x101,
        "#1020F#4PAn illusion...\x02",
    )

    CloseMessageWindow()

    label("loc_F64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1055")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEA")

    ChrTalk(    #17
        0x108,
        (
            "#072F#4PI suspect there's someone or\x01",
            "something waiting for us ahead.\x02\x03",

            "We should prepare ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1052")

    label("loc_FEA")


    ChrTalk(    #18
        0x108,
        (
            "#072F#2PI suspect there's someone or\x01",
            "something waiting for us ahead.\x02\x03",

            "We should prepare ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1052")

    Jump("loc_1381")

    label("loc_1055")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1168")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EC")

    ChrTalk(    #19
        0x106,
        (
            "#057F#4PKnowin' these idiots, there's some\x01",
            "kind of trap ahead.\x02\x03",

            "Let's make sure we're ready before\x01",
            "headin' forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1165")

    label("loc_10EC")


    ChrTalk(    #20
        0x106,
        (
            "#057F#2PKnowin' these idiots, there's some\x01",
            "kind of trap ahead.\x02\x03",

            "Let's make sure we're ready before\x01",
            "headin' forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1165")

    Jump("loc_1381")

    label("loc_1168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1291")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120A")

    ChrTalk(    #21
        0x104,
        (
            "#032F#4PThe stench of a trap ahead is so thick\x01",
            "it overwhelms the cool scents of the\x01",
            "forest.\x02\x03",

            "We should ensure we are prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128E")

    label("loc_120A")


    ChrTalk(    #22
        0x104,
        (
            "#032F#2PThe stench of a trap ahead is so thick\x01",
            "it overwhelms the cool scents of the\x01",
            "forest.\x02\x03",

            "We should ensure we are prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128E")

    Jump("loc_1381")

    label("loc_1291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1381")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1318")

    ChrTalk(    #23
        0x105,
        (
            "#042F#4PWith us off our guard, the time is ripe\x01",
            "for an ambush.\x02\x03",

            "We should make sure we're prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1381")

    label("loc_1318")


    ChrTalk(    #24
        0x105,
        (
            "#042F#2PWith us off our guard, the time is ripe\x01",
            "for an ambush.\x02\x03",

            "We should make sure we're prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1381")

    OP_A2(0x1827)
    EventEnd(0x0)
    Return()

    # Function_5_CDE end

    def Function_6_1387(): pass

    label("Function_6_1387")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B0")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)
    FadeToBright(0, 0)

    label("loc_13B0")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_13D7():
        OP_6D(-44910, 50, 22880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13D7)

    def lambda_13EF():
        OP_67(0, 6000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13EF)

    def lambda_1407():
        OP_6C(27000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1407)
    OP_6E(189, 6000)
    Fade(500)
    SetChrPos(0x101, -47410, 40, 12900, 0)
    SetChrPos(0x103, -46420, 0, 12900, 0)
    SetChrPos(0xF8, -47480, -60, 11600, 0)
    SetChrPos(0xF9, -46420, -60, 11600, 0)
    OP_6D(-46210, -40, 15430, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x101,
        "#1020F#2PHey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        "#022F#2PSure enough, a Gospel.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_154C")

    ChrTalk(    #27
        0x107,
        (
            "#065F#2PThere's fog forming on the water!\x02\x03",

            "M-Maybe this is where the fog\x01",
            "is coming from?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C6")

    label("loc_154C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B7")

    ChrTalk(    #28
        0x105,
        (
            "#043F#2PFog seems to be pouring from the\x01",
            "water's surface...\x02\x03",

            "This may be the source.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C6")

    label("loc_15B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1645")

    ChrTalk(    #29
        0x104,
        (
            "#032F#2PMist pours from the heart of the\x01",
            "wald like an endless tide.\x02\x03",

            "I suspect this is what we have\x01",
            "been searching for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16C6")

    label("loc_1645")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16C6")

    ChrTalk(    #30
        0x106,
        (
            "#057F#2PThat is a helluva lot of fog on\x01",
            "the water's surface.\x02\x03",

            "Bet this is where our troubles are\x01",
            "comin' from.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C6")


    ChrTalk(    #31
        0x101,
        (
            "#1005F#2PWe need to remove that Gospel,\x01",
            "right now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        "#024F#2PWait, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)

    def lambda_173D():
        OP_6D(-46100, -20, 16980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_173D)

    def lambda_1755():
        OP_67(0, 5380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1755)

    def lambda_176D():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_176D)

    def lambda_177D():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_177D)

    def lambda_178D():
        OP_6E(299, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_178D)
    OP_22(0x211, 0x0, 0x64)
    LoadEffect(0x0, "scraft\\sc040_08.eff")
    PlayEffect(0x0, 0x0, 0xFF, -46660, 1000, 19260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x101, 0)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#1020F#2PWaaah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_82(0x0, 0x2)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -49000, 1200, 16600, 180)
    SetChrPos(0x9, -45910, 1200, 16600, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_186F():
        OP_8F(0xFE, 0xFFFF4098, 0x2BC, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_186F)

    def lambda_188A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_188A)
    Sleep(800)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_18AB():
        OP_8F(0xFE, 0xFFFF4CAA, 0x258, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18AB)

    def lambda_18C6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18C6)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_197E")

    label("loc_1940")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1967")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_197E")

    label("loc_1967")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_197E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A5")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19E3")

    label("loc_19A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19CC")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19E3")

    label("loc_19CC")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19E3")

    Sleep(500)
    OP_1D(0x29)
    Sleep(1000)

    ChrTalk(    #35
        0x101,
        "#1020F#2PMore fog monsters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#022F#2PThey're quite a bit more powerful-\x01",
            "looking than the ones from the farm.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB2")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 22)
    SetChrSubChip(0x104, 0)
    Jump("loc_1B3F")

    label("loc_1AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD6")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 20)
    SetChrSubChip(0x105, 0)
    Jump("loc_1B3F")

    label("loc_1AD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AFA")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    Jump("loc_1B3F")

    label("loc_1AFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B1E")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    Jump("loc_1B3F")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3F")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)

    label("loc_1B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B63")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 22)
    SetChrSubChip(0x104, 0)
    Jump("loc_1BF0")

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B87")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 20)
    SetChrSubChip(0x105, 0)
    Jump("loc_1BF0")

    label("loc_1B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAB")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    Jump("loc_1BF0")

    label("loc_1BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BCF")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    Jump("loc_1BF0")

    label("loc_1BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BF0")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)

    label("loc_1BF0")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(    #37
        0x106,
        "#054F#2PFine by me! BRING IT!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA9")

    label("loc_1C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(    #38
        0x108,
        "#076F#2PHere they come!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA9")

    label("loc_1C53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C83")

    ChrTalk(    #39
        0x105,
        "#042F#2PBrace yourselves!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA9")

    label("loc_1C83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA9")

    ChrTalk(    #40
        0x104,
        "#032F#2PThey come!\x02",
    )

    CloseMessageWindow()

    label("loc_1CA9")

    Sleep(500)

    def lambda_1CB4():
        OP_6D(-45350, -50, 14500, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CB4)

    def lambda_1CCC():
        OP_6B(2680, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CCC)
    SetChrChipByIndex(0x8, 27)

    def lambda_1CE1():
        OP_8E(0xFE, 0xFFFF453E, 0xC8, 0x3390, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1CE1)
    Sleep(50)
    SetChrChipByIndex(0x9, 26)

    def lambda_1D06():
        OP_8E(0xFE, 0xFFFF4CBE, 0xC8, 0x3232, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1D06)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0x45F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1D51"),
        (SWITCH_DEFAULT, "loc_1D56"),
    )


    label("loc_1D51")

    OP_B4(0x0)
    Jump("loc_1D56")

    label("loc_1D56")

    Call(0, 7)
    Return()

    # Function_6_1387 end

    def Function_7_1D5B(): pass

    label("Function_7_1D5B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, -47410, 40, 12950, 0)
    SetChrPos(0x103, -46420, 0, 12860, 0)
    SetChrPos(0xF8, -47480, -60, 11470, 0)
    SetChrPos(0xF9, -46420, -60, 11450, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, -47410, 40, 12900, 0)
    SetChrPos(0x103, -46420, 0, 12900, 0)
    SetChrPos(0xF8, -47480, -60, 11600, 0)
    SetChrPos(0xF9, -46420, -60, 11600, 0)
    OP_6D(-46210, -40, 15430, 0)
    OP_67(0, 6510, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x101,
        (
            "#1007F#2P*pant* *pant*\x02\x03",

            "#1019FOkay... Almost murdered by fog...\x01",
            "but we're alive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x103,
        (
            "#024F#2PDon't let your guard down!\x01",
            "Those were just phantoms!\x02\x03",

            "The person who controlled them\x01",
            "is around here somewhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1004F#2PBut where?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #44
        "\x07\x05You've done very well.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #45
        (
            "\x07\x05Your efforts deserve a reward, and I...\x01",
            "shall give you the sweetest I am able.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #46
        0x103,
        "#022F#2P*gasp*\x02",
    )

    CloseMessageWindow()
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    OP_20(0x7D0)

    def lambda_2018():
        OP_6D(-45170, 20, 19670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2018)

    def lambda_2030():
        OP_67(0, 5380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2030)

    def lambda_2048():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2048)

    def lambda_2058():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2058)

    def lambda_2068():
        OP_6E(299, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2068)
    Sleep(2500)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    WaitChrThread(0x101, 0x1)
    OP_1D(0x5C)
    Sleep(1000)
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -46500, 2800, 19600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #47
        0x101,
        "#1020F#2PWhat the--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        "#523F#2PNo!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_C0(0x14, 0x1388, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x1388)
    OP_24(0x90, 0x5A)
    Sleep(400)
    OP_24(0x90, 0x50)
    Sleep(400)
    OP_24(0x90, 0x46)
    Sleep(400)
    OP_24(0x90, 0x3C)
    Sleep(400)
    OP_24(0x90, 0x32)
    Sleep(400)
    OP_24(0x90, 0x28)
    Sleep(400)
    OP_24(0x90, 0x1E)
    Sleep(400)
    OP_24(0x90, 0x14)
    Sleep(400)
    OP_23(0x90)
    OP_0D()
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_21A0"),
        (6, "loc_21A6"),
        (3, "loc_21AC"),
        (4, "loc_21B2"),
        (7, "loc_21B8"),
        (SWITCH_DEFAULT, "loc_21BE"),
    )


    label("loc_21A0")

    OP_A2(0x1829)
    Jump("loc_21BE")

    label("loc_21A6")

    OP_A2(0x182A)
    Jump("loc_21BE")

    label("loc_21AC")

    OP_A2(0x182B)
    Jump("loc_21BE")

    label("loc_21B2")

    OP_A2(0x182C)
    Jump("loc_21BE")

    label("loc_21B8")

    OP_A2(0x182D)
    Jump("loc_21BE")

    label("loc_21BE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_21DB"),
        (6, "loc_21E1"),
        (3, "loc_21E7"),
        (4, "loc_21ED"),
        (7, "loc_21F3"),
        (SWITCH_DEFAULT, "loc_21F9"),
    )


    label("loc_21DB")

    OP_A2(0x182E)
    Jump("loc_21F9")

    label("loc_21E1")

    OP_A2(0x182F)
    Jump("loc_21F9")

    label("loc_21E7")

    OP_A2(0x1830)
    Jump("loc_21F9")

    label("loc_21ED")

    OP_A2(0x1831)
    Jump("loc_21F9")

    label("loc_21F3")

    OP_A2(0x1832)
    Jump("loc_21F9")

    label("loc_21F9")

    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1828)
    OP_28(0x92, 0x1, 0x20)
    OP_28(0x92, 0x1, 0x40)
    OP_28(0x92, 0x1, 0x80)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1D5B end

    def Function_8_2232(): pass

    label("Function_8_2232")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24AE")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Before being alone, Agate was Partner 2\x01",        # 0
            "Before being alone, Tita was Partner 2\x01",         # 1
            "Before being alone, Olivier was Partner 2\x01",      # 2
            "Before being alone, Kloe was Partner 2\x01",         # 3
            "Before being alone, Agate was Partner 2\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_236A"),
        (1, "loc_2370"),
        (2, "loc_2376"),
        (3, "loc_237C"),
        (4, "loc_2382"),
        (SWITCH_DEFAULT, "loc_2388"),
    )


    label("loc_236A")

    OP_A2(0x1829)
    Jump("loc_2388")

    label("loc_2370")

    OP_A2(0x182A)
    Jump("loc_2388")

    label("loc_2376")

    OP_A2(0x182B)
    Jump("loc_2388")

    label("loc_237C")

    OP_A2(0x182C)
    Jump("loc_2388")

    label("loc_2382")

    OP_A2(0x182D)
    Jump("loc_2388")

    label("loc_2388")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Before being alone, Agate was Partner 3\x01",        # 0
            "Before being alone, Tita was Partner 3\x01",         # 1
            "Before being alone, Olivier was Partner 3\x01",      # 2
            "Before being alone, Kloe was Partner 3\x01",         # 3
            "Before being alone, Agate was Partner 3\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2490"),
        (1, "loc_2496"),
        (2, "loc_249C"),
        (3, "loc_24A2"),
        (4, "loc_24A8"),
        (SWITCH_DEFAULT, "loc_24AE"),
    )


    label("loc_2490")

    OP_A2(0x182E)
    Jump("loc_24AE")

    label("loc_2496")

    OP_A2(0x182F)
    Jump("loc_24AE")

    label("loc_249C")

    OP_A2(0x1830)
    Jump("loc_24AE")

    label("loc_24A2")

    OP_A2(0x1831)
    Jump("loc_24AE")

    label("loc_24A8")

    OP_A2(0x1832)
    Jump("loc_24AE")

    label("loc_24AE")

    AddParty(0x2, 0xF7, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 1)), scpexpr(EXPR_END)), "loc_24C0")
    AddParty(0x5, 0xF8, 0xFF)
    Jump("loc_24F5")

    label("loc_24C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 2)), scpexpr(EXPR_END)), "loc_24CE")
    AddParty(0x6, 0xF8, 0xFF)
    Jump("loc_24F5")

    label("loc_24CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 3)), scpexpr(EXPR_END)), "loc_24DC")
    AddParty(0x3, 0xF8, 0xFF)
    Jump("loc_24F5")

    label("loc_24DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 4)), scpexpr(EXPR_END)), "loc_24EA")
    AddParty(0x4, 0xF8, 0xFF)
    Jump("loc_24F5")

    label("loc_24EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 5)), scpexpr(EXPR_END)), "loc_24F5")
    AddParty(0x7, 0xF8, 0xFF)

    label("loc_24F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 6)), scpexpr(EXPR_END)), "loc_2503")
    AddParty(0x5, 0xF9, 0xFF)
    Jump("loc_2538")

    label("loc_2503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 7)), scpexpr(EXPR_END)), "loc_2511")
    AddParty(0x6, 0xF9, 0xFF)
    Jump("loc_2538")

    label("loc_2511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 0)), scpexpr(EXPR_END)), "loc_251F")
    AddParty(0x3, 0xF9, 0xFF)
    Jump("loc_2538")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 1)), scpexpr(EXPR_END)), "loc_252D")
    AddParty(0x4, 0xF9, 0xFF)
    Jump("loc_2538")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 2)), scpexpr(EXPR_END)), "loc_2538")
    AddParty(0x7, 0xF9, 0xFF)

    label("loc_2538")

    OP_6D(-46680, 20, 12540, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    SetChrPos(0x101, -47720, 20, 12910, 0)
    SetChrPos(0x103, -46230, -20, 13170, 270)
    SetChrPos(0xF8, -47480, -60, 11470, 0)
    SetChrPos(0xF9, -46420, -60, 11450, 0)

    NpcTalk(    #49
        0x103,
        "Woman's Voice",
        "#2PEstelle! Wake up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1007F#6PMmph...\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_2619"),
        (6, "loc_2621"),
        (3, "loc_2629"),
        (4, "loc_2631"),
        (7, "loc_2639"),
        (SWITCH_DEFAULT, "loc_2641"),
    )


    label("loc_2619")

    SetChrChipByIndex(0xF8, 4)
    Jump("loc_2641")

    label("loc_2621")

    SetChrChipByIndex(0xF8, 5)
    Jump("loc_2641")

    label("loc_2629")

    SetChrChipByIndex(0xF8, 6)
    Jump("loc_2641")

    label("loc_2631")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_2641")

    label("loc_2639")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_2641")

    label("loc_2641")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_265E"),
        (6, "loc_2666"),
        (3, "loc_266E"),
        (4, "loc_2676"),
        (7, "loc_267E"),
        (SWITCH_DEFAULT, "loc_2686"),
    )


    label("loc_265E")

    SetChrChipByIndex(0xF9, 4)
    Jump("loc_2686")

    label("loc_2666")

    SetChrChipByIndex(0xF9, 5)
    Jump("loc_2686")

    label("loc_266E")

    SetChrChipByIndex(0xF9, 6)
    Jump("loc_2686")

    label("loc_2676")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_2686")

    label("loc_267E")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_2686")

    label("loc_2686")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x101,
        "#1026F#6PHuh? Schera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        (
            "#023F#4PEstelle?!\x02\x03",

            "#524FThank Aidios, you woke up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1025F#6PAh. Yeah...\x02\x03",

            "It was like...a really long dream.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 180, 400)
    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        (
            "#1017F#6PNow I get it.\x02\x03",

            "It's because of this...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1005F#6PHEY! GUYS!\x01",
            "Happy dream time is over!\x02\x03",

            "Come on! Back to reality!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        "#023F#4PEstelle?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_283A")

    ChrTalk(    #57
        0x107,
        "#561FNn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_283A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_285C")

    ChrTalk(    #58
        0x106,
        "#056FGuh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_285C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2883")

    ChrTalk(    #59
        0x104,
        "#034FMmmnnnnn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_2883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A4")

    ChrTalk(    #60
        0x105,
        "#049FAh...\x02",
    )

    CloseMessageWindow()
    Jump("loc_28C2")

    label("loc_28A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C2")

    ChrTalk(    #61
        0x108,
        "#572FMmmh.\x02",
    )

    CloseMessageWindow()

    label("loc_28C2")

    OP_9E(0xF8, 0xF, 0x0, 0x12C, 0xFA0)
    Fade(500)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0xF9, 0xF, 0x0, 0x12C, 0xFA0)
    Fade(500)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293D")

    ChrTalk(    #62
        0x107,
        "#064FHuh? Estelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C2")

    label("loc_293D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2969")

    ChrTalk(    #63
        0x105,
        "#044FAh... Estelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C2")

    label("loc_2969")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299E")

    ChrTalk(    #64
        0x104,
        "#033FWho... Es...telle? How...\x02",
    )

    CloseMessageWindow()
    Jump("loc_29C2")

    label("loc_299E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C2")

    ChrTalk(    #65
        0x106,
        "#052F...Estelle?\x02",
    )

    CloseMessageWindow()

    label("loc_29C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A00")

    ChrTalk(    #66
        0x108,
        (
            "#572FI was trapped in a dream...\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABC")

    label("loc_2A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A40")

    ChrTalk(    #67
        0x106,
        (
            "#552FRight... Of course that was\x01",
            "a dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABC")

    label("loc_2A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7D")

    ChrTalk(    #68
        0x104,
        (
            "#032FA dream?\x01",
            "Trapped in a dream. Hmm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ABC")

    label("loc_2A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ABC")

    ChrTalk(    #69
        0x105,
        (
            "#049FIt was all...just a dream?\x01",
            "I... I see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ABC")


    ChrTalk(    #70
        0x101,
        "#1006F#6PThank goodness! You're awake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x103,
        (
            "#524F#4PYou still surprise me sometimes,\x01",
            "Estelle.\x02\x03",

            "Not only did you wake up on\x01",
            "your own, but you woke the\x01",
            "others as well.\x02\x03",

            "#026FNow, then. With that settled...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    Sleep(500)

    ChrTalk(    #72
        0x103,
        (
            "#024F#4P#3SYou're there, aren't you?\x01",
            "Show yourself, Luciola!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #73
        0x101,
        "#1004F#6PWhat?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #74
        (
            "\x07\x05Heehee...\x01",
            "You have called for me at last.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    OP_1D(0x6F)
    Sleep(300)

    def lambda_2C83():
        OP_6D(-45560, -10, 16980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C83)

    def lambda_2C9B():
        OP_67(0, 5240, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C9B)

    def lambda_2CB3():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2CB3)

    def lambda_2CC3():
        OP_6E(325, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CC3)

    def lambda_2CD3():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2CD3)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xC, -46320, 70, 19130, 180)

    def lambda_2D15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2D15)
    OP_22(0x99, 0x0, 0x64)
    OP_43(0xA, 0x1, 0x0, 0xA)
    OP_43(0xB, 0x1, 0x0, 0xB)
    OP_82(0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D75")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DB3")

    label("loc_2D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9C")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2DB3")

    label("loc_2D9C")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DDA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E18")

    label("loc_2DDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E01")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2E18")

    label("loc_2E01")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2E18")

    Sleep(1000)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #75
        0x101,
        "#1020F#2PWha?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        "#022F#2PI knew it.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #77
        0xC,
        "Woman in Black",
        (
            "#240FIt has been a very, very long time,\x01",
            "Scherazard.\x02\x03",

            "Eight years or more, now, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x103,
        (
            "#522F#2PAbout that, yes.\x02\x03",

            "To think you would ever be\x01",
            "responsible for something like this...\x02\x03",

            "#022FWhat are you doing, Luci?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 0, 500)
    Sleep(500)

    ChrTalk(    #79
        0x101,
        (
            "#1020F#2PWait, wait, WAIT! Hold on!\x02\x03",

            "Schera, you...KNOW this person?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0xC,
        "Woman in Black",
        (
            "#241FWhy, Estelle, sweetheart!\x01",
            "That hurts.\x02\x03",

            "Have you forgotten me so quickly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1004F#2PWhat in the world do you mean?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0xC,
        "Woman in Black",
        (
            "#241FThe nice lady who showed you all\x01",
            "those wonderful tarot card games,\x01",
            "and read your fortune...\x02\x03",

            "Don't you remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1020F#2P...WHA?!\x02",
    )

    CloseMessageWindow()
    OP_AD(0x24007D, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #84
        0x101,
        (
            "#1020F#2PBut she was... No way...\x02\x03",

            "You're...MISS LUCI?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #85
        0xC,
        "Woman in Black",
        (
            "#241FWell...that is who\x01",
            "I was, once.\x02",
        )
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS117._CH")
    OP_C6(0x0, 0x0, 125000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Woman in Black")

    AnonymousTalk(    #86
        (
            "\x07\x00#241FBut now...my purpose is different.\x02\x03",

            "Now I am Enforcer No. VI to the Grandmaster of Ouroboros--\x01",
            "Luciola the Bewitching Bell.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)
    OP_C6(0x0, 0x6, 0, 0, 0)

    ChrTalk(    #87
        0x101,
        "#1020F#2PBut... But why? How?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "#240FI would imagine Schera has\x01",
            "figured it out, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        (
            "#026F#2PIllusion magic using a bell--\x01",
            "your specialty, Luci.\x02\x03",

            "#022FI hope you won't try to tell me\x01",
            "the fog all over Rolent is an illusion,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xC,
        (
            "#241FNo, no, of course not.\x02\x03",

            "That was a phenomenon\x01",
            "caused by the Gospel.\x02\x03",

            "It has worked well as...a catalyst,\x01",
            "of sorts, to interfere with dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x103,
        (
            "#023F#2PA...cata...\x02\x03",

            "#024FAre you saying the Gospel can\x01",
            "affect the human mind?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "#240FIt seems it can.\x02\x03",

            "My bell was little more than a guiding hand.\x02\x03",

            "The Gospel, the fog, and the bell together\x01",
            "create a dream so real that 'illusions'\x01",
            "cannot compare.\x02\x03",

            "#244FA simple, happy dream, bereft of suffering\x01",
            "and loneliness. A dream you wish was real.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_359F")

    ChrTalk(    #93
        0x107,
        "#063FB-B-But that's...\x02",
    )

    CloseMessageWindow()

    label("loc_359F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35CC")

    ChrTalk(    #94
        0x106,
        "#552FThe hell kind of...?\x02",
    )

    CloseMessageWindow()

    label("loc_35CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3620")

    ChrTalk(    #95
        0x104,
        (
            "#032FDreams are...not a toy for you to abuse,\x01",
            "pawn of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_363C")

    ChrTalk(    #96
        0x105,
        "#043F...\x02",
    )

    CloseMessageWindow()

    label("loc_363C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366A")

    ChrTalk(    #97
        0x108,
        "#072FBut that is... I see.\x02",
    )

    CloseMessageWindow()

    label("loc_366A")


    ChrTalk(    #98
        0x103,
        "#522F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1002F#2PHey...'Enforcer.'\x02\x03",

            "Why is the society doing all this?\x02\x03",

            "What are you hoping to gain with these\x01",
            "bizarre experiments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        (
            "#240FI am but a servant, Estelle.\x01",
            "The striking hand of the Grandmaster and\x01",
            "the Anguis.\x02\x03",

            "In truth, I myself have been little more\x01",
            "than a catalyst for this experiment.\x02\x03",

            "You shall have to ask the professor or\x01",
            "Loewe for details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1002F#2PThe 'professor,' 'Loewe'...\x02\x03",

            "I've heard these names again and again.\x01",
            "But who ARE they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xC,
        (
            "#241FYou will see, when the time comes.\x01",
            "Which may not be far off now.\x02\x03",

            "It is ironic, though...\x01",
            "You've met them both before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1004F#2PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        (
            "#522F#2P...\x02\x03",

            "Luci. May I say one thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        "#243FOh? Of course.\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #106
        0x103,
        (
            "#524F#2PAt first, I didn't intend to stay in\x01",
            "Liberl for long.\x02\x03",

            "I was simply looking for a place to...\x01",
            "run away to, really...until you came back.\x02\x03",

            "#026FBut now, it's been eight years.\x02\x03",

            "Now I have friends, companions...\x01",
            "people I consider family...a job I'm proud of.\x02\x03",

            "#022FI am no longer the dancing girl\x01",
            "Schera of the Harvey troupe.\x01",
            "I am Scherazard Harvey, the bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1026F#2PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xC,
        "#242F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        "#026F#2PThis new home of mine...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #110
        0x103,
        (
            "#024F#2PI will not allow anyone to harm it--\x01",
            "not even you, Luci!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #111
        0xC,
        (
            "#244FHeehee... Good. Your spirit\x01",
            "is as strong as ever, Scherazard.\x02\x03",

            "#241FAnd the power of the society grows\x01",
            "enormous--even more so with the\x01",
            "power of the Gospels.\x02\x03",

            "If you wish to oppose us, you will\x01",
            "need everything you have.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    Fade(1000)
    OP_71(0x0, 0x4)
    OP_22(0x82, 0x0, 0x64)
    OP_0D()
    OP_43(0xA, 0x1, 0x0, 0xC)
    OP_43(0xB, 0x1, 0x0, 0xD)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #112
        0x101,
        "#1004F#2PAaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x103,
        "#023F#2PLuci!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "#241FDon't fret...\x01",
            "We shall meet again, and soon.\x02\x03",

            "Perhaps, then, we can fill in the\x01",
            "long gaps between those lost years...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11E, 0x0, 0x64)

    def lambda_3D95():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3D95)

    def lambda_3DA7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3DA7)

    def lambda_3DB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3DB9)
    Sleep(500)

    def lambda_3DD0():
        OP_6D(-45830, 10, 17150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DD0)

    def lambda_3DE8():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DE8)
    SetChrChipByIndex(0x103, 65535)
    OP_8E(0x103, 0xFFFF49DA, 0x14, 0x42D6, 0x1388, 0x0)
    WaitChrThread(0xC, 0x2)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #115
        0x103,
        "#522F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #116
        0x101,
        "#1026F#2PSchera...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #117
        0x103,
        "#025F#6P...How maddening.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(500)

    ChrTalk(    #118
        0x103,
        (
            "#524F#6PShe's gotten away...but we've put an\x01",
            "end to the trouble.\x02\x03",

            "Those slumbering should awaken soon.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0100   ._SN", 119, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2232 end

    def Function_9_3F13(): pass

    label("Function_9_3F13")

    OP_24(0x10A, 0x5A)
    Sleep(100)
    OP_24(0x10A, 0x50)
    Sleep(100)
    OP_24(0x10A, 0x46)
    Sleep(100)
    OP_24(0x10A, 0x3C)
    Sleep(100)
    OP_24(0x10A, 0x32)
    Sleep(100)
    OP_24(0x10A, 0x28)
    Sleep(100)
    OP_24(0x10A, 0x1E)
    Sleep(100)
    OP_24(0x10A, 0x14)
    Sleep(100)
    OP_23(0x10A)
    Return()

    # Function_9_3F13 end

    def Function_10_3F5F(): pass

    label("Function_10_3F5F")

    SetChrSubChip(0xA, 0)
    SetChrPos(0xA, -46320, 70, 19130, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3F86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3F86)
    ClearChrFlags(0xA, 0x80)
    OP_91(0xA, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xA, 0x80)
    Return()

    # Function_10_3F5F end

    def Function_11_4048(): pass

    label("Function_11_4048")

    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, -46320, 70, 19130, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_406F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_406F)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0xB, 0x80)
    Return()

    # Function_11_4048 end

    def Function_12_4131(): pass

    label("Function_12_4131")

    SetChrSubChip(0xA, 0)
    SetChrPos(0xA, -46320, 70, 19130, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_91(0xA, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_41A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41DB")
    OP_91(0xA, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_41A7")

    label("loc_41DB")

    Return()

    # Function_12_4131 end

    def Function_13_41DC(): pass

    label("Function_13_41DC")

    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, -46320, 70, 19130, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_4252")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4286")
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_4252")

    label("loc_4286")

    Return()

    # Function_13_41DC end

    def Function_14_4287(): pass

    label("Function_14_4287")

    EventBegin(0x1)

    ChrTalk(    #119
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_42B3():
        OP_6D(55440, 360, 7980, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_42B3)

    def lambda_42CB():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_42CB)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #120
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441B")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x3, 0xD174, 0x17C, 0x2044, 0x5A, 0xDEC6, 0xFFFFFC18, 0x1E32)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_4415")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440C")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x40)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #121
        "\x07\x05Recorded Mistwald fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_440C")

    Jump("loc_4415")

    label("loc_440F")

    OP_28(0x73, 0x1, 0x4000)

    label("loc_4415")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_442A")

    label("loc_441B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_442A")
    EventEnd(0x1)

    label("loc_442A")

    Return()

    # Function_14_4287 end

    def Function_15_442B(): pass

    label("Function_15_442B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Set Scherazard as Partner]\x01",      # 0
            "[Set Agate as Partner]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_44AB"),
        (1, "loc_44B1"),
        (SWITCH_DEFAULT, "loc_44B7"),
    )


    label("loc_44AB")

    OP_A2(0x1200)
    Jump("loc_44B7")

    label("loc_44B1")

    OP_A2(0x1201)
    Jump("loc_44B7")

    label("loc_44B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_44C5")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_44C9")

    label("loc_44C5")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_44C9")

    Return()

    # Function_15_442B end

    def Function_16_44CA(): pass

    label("Function_16_44CA")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_16_44CA end

    SaveToFile()

Try(main)
