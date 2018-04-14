from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '气雾兽',                               # 9
        '无形迷雾',                             # 10
        '残像',                                 # 11
        '残像',                                 # 12
        '幻惑之铃露茜奥拉',                     # 13
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
        "Function_4_A18",          # 04, 4
        "Function_5_CCB",          # 05, 5
        "Function_6_107A",         # 06, 6
        "Function_7_199E",         # 07, 7
        "Function_8_1E1D",         # 08, 8
        "Function_9_370B",         # 09, 9
        "Function_10_3757",        # 0A, 10
        "Function_11_3840",        # 0B, 11
        "Function_12_3929",        # 0C, 12
        "Function_13_39D4",        # 0D, 13
        "Function_14_3A7F",        # 0E, 14
        "Function_15_3C0B",        # 0F, 15
        "Function_16_3CA7",        # 10, 16
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
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
            "#1000F◆哇哇……\x01",
            "好浓的雾，什么都看不见。\x02\x03",

            "◆怎么办？雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#020F◆……没办法。\x01",
            "　\x09只能原路返回了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_84B)
    Sleep(50)

    def lambda_86B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_86B)
    Sleep(100)

    def lambda_88B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_88B)
    Sleep(50)

    def lambda_8AB():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8AB)
    OP_A2(0x1841)
    NewScene("ED6_DT21/C0301   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_A17")

    label("loc_8CF")

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
            "#020F◆制雾器\x01",
            "　反复的消息哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_999():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_999)
    Sleep(50)

    def lambda_9B9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA84, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_9B9)
    Sleep(100)

    def lambda_9D9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9D9)
    Sleep(50)

    def lambda_9F9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFEA20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9F9)
    NewScene("ED6_DT21/C0301   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_A17")

    Return()

    # Function_3_685 end

    def Function_4_A18(): pass

    label("Function_4_A18")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)

    label("loc_A38")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B27")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B65")

    label("loc_B27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B65")

    label("loc_B4E")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8C")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BCA")

    label("loc_B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB3")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_BCA")

    label("loc_BB3")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_BCA")

    OP_20(0xBB8)
    StopSound(0x64, 0x2710, 0x1770)
    Sleep(3000)

    ChrTalk(    #3
        0x101,
        "#1020F#5P哇哇……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1A")

    ChrTalk(    #4
        0x108,
        "#072F呼……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #5
        0x106,
        "#057F可恶……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C60")

    ChrTalk(    #6
        0x104,
        "#033F噢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C82")

    ChrTalk(    #7
        0x105,
        "#043F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA5")

    label("loc_C82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA5")

    ChrTalk(    #8
        0x107,
        "#065F啊哇哇……\x02",
    )

    CloseMessageWindow()

    label("loc_CA5")


    ChrTalk(    #9
        0x103,
        "#523F#6P喔……\x02",
    )

    CloseMessageWindow()
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0304   ._SN", 100, 20, 0)
    IdleLoop()
    Return()

    # Function_4_A18 end

    def Function_5_CCB(): pass

    label("Function_5_CCB")

    EventBegin(0x4)
    FadeToDark(0, 16777215, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF5")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)

    label("loc_CF5")

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
        "#1025F#5P回、回来了…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#022F#6P这里是……\x01",
            "似乎离赛尔贝大树很近了。\x02\x03",

            "#026F看来刚才似乎是陷入『结界』\x01",
            "中了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x316, 0)), scpexpr(EXPR_END)), "loc_F14")

    ChrTalk(    #12
        0x101,
        "#1020F#5P结、结界……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x101,
        (
            "#1005F#5P难、难道是……\x02\x03",

            "通往赛尔贝大树之路的消失\x01",
            "也是因为……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 90, 400)
    Sleep(500)

    ChrTalk(    #14
        0x103,
        (
            "#524F#6P呵呵……\x01",
            "你也注意到了啊。\x02\x03",

            "大概是结界让我们产生了幻觉，\x01",
            "无法看到正确的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1020F#5P怎、怎会有这种事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_F2F")

    label("loc_F14")


    ChrTalk(    #16
        0x101,
        "#1020F#5P结、结界……\x02",
    )

    CloseMessageWindow()

    label("loc_F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F7B")

    ChrTalk(    #17
        0x108,
        (
            "#072F#4P也许前面\x01",
            "会有机关吧，\x02\x03",

            "做好准备再继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1074")

    label("loc_F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(    #18
        0x106,
        (
            "#057F#4P大概前面\x01",
            "还会有机关。\x02\x03",

            "做好准备再继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1074")

    label("loc_FC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1011")

    ChrTalk(    #19
        0x104,
        (
            "#032F#4P也许前面\x01",
            "会有机关，\x02\x03",

            "做好准备再继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1074")

    label("loc_1011")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1074")

    ChrTalk(    #20
        0x105,
        (
            "#042F#4P如果不出所料的话，前面\x01",
            "也许会有机关也说不定，\x02\x03",

            "做好准备之后继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1074")

    OP_A2(0x1827)
    EventEnd(0x0)
    Return()

    # Function_5_CCB end

    def Function_6_107A(): pass

    label("Function_6_107A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A3")
    Call(0, 15)
    FadeToBright(0, 0)
    Call(0, 16)
    FadeToBright(0, 0)

    label("loc_10A3")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_10CA():
        OP_6D(-44910, 50, 22880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10CA)

    def lambda_10E2():
        OP_67(0, 6000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10E2)

    def lambda_10FA():
        OP_6C(27000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10FA)
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

    ChrTalk(    #21
        0x101,
        "#1020F#6P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        "#022F#4P果然是『福音』……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1222")

    ChrTalk(    #23
        0x107,
        (
            "#065F#4P从水面上升起的雾……\x02\x03",

            "也许那些雾就是在这里\x01",
            "产生的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_1222")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1276")

    ChrTalk(    #24
        0x105,
        (
            "#043F#4P水面上冒着雾气……\x02\x03",

            "说不定那些雾就是在这里\x01",
            "产生的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_1276")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12CE")

    ChrTalk(    #25
        0x104,
        (
            "#032F#4P水面上冒着雾气……\x02\x03",

            "原来如此，那些雾就是在这里\x01",
            "产生的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1321")

    label("loc_12CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1321")

    ChrTalk(    #26
        0x106,
        (
            "#057F#4P水面上冒着雾气……\x02\x03",

            "难道说…那些雾就是在这里\x01",
            "产生的吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1321")


    ChrTalk(    #27
        0x101,
        (
            "#1005F#6P那、那样的话\x01",
            "我们就赶快把『福音』取下来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        "#024F#4P艾丝蒂尔！慢着！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)

    def lambda_139C():
        OP_6D(-46100, -20, 16980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_139C)

    def lambda_13B4():
        OP_67(0, 5380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B4)

    def lambda_13CC():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13CC)

    def lambda_13DC():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13DC)

    def lambda_13EC():
        OP_6E(299, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13EC)
    OP_22(0x211, 0x0, 0x64)
    LoadEffect(0x0, "scraft\\sc040_08.eff")
    PlayEffect(0x0, 0x0, 0xFF, -46660, 1000, 19260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x101, 0)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        "#1020F#6P哇啊……！？\x02",
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

    def lambda_14D4():
        OP_8F(0xFE, 0xFFFF4098, 0x2BC, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14D4)

    def lambda_14EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14EF)
    Sleep(800)
    OP_22(0x211, 0x0, 0x64)
    OP_22(0x215, 0x0, 0x64)

    def lambda_1510():
        OP_8F(0xFE, 0xFFFF4CAA, 0x258, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1510)

    def lambda_152B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_152B)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(800)
    OP_22(0x21A, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A5")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15E3")

    label("loc_15A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CC")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_15E3")

    label("loc_15CC")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_15E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160A")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1648")

    label("loc_160A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1631")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1648")

    label("loc_1631")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1648")

    Sleep(500)
    OP_1D(0x29)
    Sleep(1000)

    ChrTalk(    #31
        0x101,
        "#1020F#6P这、这些是什么东西！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        (
            "#022F#4P这两只怪物似乎比我们在\x01",
            "农场打倒的那些强得多……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1702")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 22)
    SetChrSubChip(0x104, 0)
    Jump("loc_178F")

    label("loc_1702")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1726")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 20)
    SetChrSubChip(0x105, 0)
    Jump("loc_178F")

    label("loc_1726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174A")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    Jump("loc_178F")

    label("loc_174A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176E")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    Jump("loc_178F")

    label("loc_176E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178F")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)

    label("loc_178F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B3")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 22)
    SetChrSubChip(0x104, 0)
    Jump("loc_1840")

    label("loc_17B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D7")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 20)
    SetChrSubChip(0x105, 0)
    Jump("loc_1840")

    label("loc_17D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FB")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x108, 24)
    SetChrSubChip(0x108, 0)
    Jump("loc_1840")

    label("loc_17FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181F")
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    Jump("loc_1840")

    label("loc_181F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1840")
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 14)
    SetChrSubChip(0x106, 0)

    label("loc_1840")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186E")

    ChrTalk(    #33
        0x106,
        "#054F#4P……它们来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_186E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1897")

    ChrTalk(    #34
        0x108,
        "#076F#4P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_1897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C4")

    ChrTalk(    #35
        0x105,
        "#042F#4P……它们来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_18C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EC")

    ChrTalk(    #36
        0x104,
        "#032F#4P……要来了！\x02",
    )

    CloseMessageWindow()

    label("loc_18EC")

    Sleep(500)

    def lambda_18F7():
        OP_6D(-45350, -50, 14500, 300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F7)

    def lambda_190F():
        OP_6B(2680, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_190F)
    SetChrChipByIndex(0x8, 27)

    def lambda_1924():
        OP_8E(0xFE, 0xFFFF453E, 0xC8, 0x3390, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1924)
    Sleep(50)
    SetChrChipByIndex(0x9, 26)

    def lambda_1949():
        OP_8E(0xFE, 0xFFFF4CBE, 0xC8, 0x3232, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1949)
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
        (1, "loc_1994"),
        (SWITCH_DEFAULT, "loc_1999"),
    )


    label("loc_1994")

    OP_B4(0x0)
    Jump("loc_1999")

    label("loc_1999")

    Call(0, 7)
    Return()

    # Function_6_107A end

    def Function_7_199E(): pass

    label("Function_7_199E")

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

    ChrTalk(    #37
        0x101,
        (
            "#1007F#6P呼、呼……\x02\x03",

            "#1019F真、真没想到竟然\x01",
            "会这么难缠……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#024F#4P不要大意啊！\x01",
            "刚才我们打倒的只是召唤出来的妖物！\x02\x03",

            "操纵它们的施术者\x01",
            "应该还藏在附近！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1004F#6P什么……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #40
        (
            "\x07\x05呵呵……\x01",
            "你们还挺努力的嘛，\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        (
            "\x07\x05既然如此的话我就\x01",
            "奖励你们一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #42
        0x103,
        "#022F#4P！！！\x02",
    )

    CloseMessageWindow()
    OP_22(0x118, 0x0, 0x64)
    Sleep(500)
    OP_20(0x7D0)

    def lambda_1BFC():
        OP_6D(-45170, 20, 19670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BFC)

    def lambda_1C14():
        OP_67(0, 5380, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C14)

    def lambda_1C2C():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C2C)

    def lambda_1C3C():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C3C)

    def lambda_1C4C():
        OP_6E(299, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1C4C)
    Sleep(2500)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    WaitChrThread(0x101, 0x1)
    OP_1D(0x5C)
    Sleep(1000)
    OP_22(0x90, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, -46500, 2800, 19600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #43
        0x101,
        "#1020F#5P什…什么…！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x103,
        "#523F#2P糟了……！\x02",
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
        (5, "loc_1D8B"),
        (6, "loc_1D91"),
        (3, "loc_1D97"),
        (4, "loc_1D9D"),
        (7, "loc_1DA3"),
        (SWITCH_DEFAULT, "loc_1DA9"),
    )


    label("loc_1D8B")

    OP_A2(0x1829)
    Jump("loc_1DA9")

    label("loc_1D91")

    OP_A2(0x182A)
    Jump("loc_1DA9")

    label("loc_1D97")

    OP_A2(0x182B)
    Jump("loc_1DA9")

    label("loc_1D9D")

    OP_A2(0x182C)
    Jump("loc_1DA9")

    label("loc_1DA3")

    OP_A2(0x182D)
    Jump("loc_1DA9")

    label("loc_1DA9")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_1DC6"),
        (6, "loc_1DCC"),
        (3, "loc_1DD2"),
        (4, "loc_1DD8"),
        (7, "loc_1DDE"),
        (SWITCH_DEFAULT, "loc_1DE4"),
    )


    label("loc_1DC6")

    OP_A2(0x182E)
    Jump("loc_1DE4")

    label("loc_1DCC")

    OP_A2(0x182F)
    Jump("loc_1DE4")

    label("loc_1DD2")

    OP_A2(0x1830)
    Jump("loc_1DE4")

    label("loc_1DD8")

    OP_A2(0x1831)
    Jump("loc_1DE4")

    label("loc_1DDE")

    OP_A2(0x1832)
    Jump("loc_1DE4")

    label("loc_1DE4")

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

    # Function_7_199E end

    def Function_8_1E1D(): pass

    label("Function_8_1E1D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2087")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2087")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇队伍变成１人之前，阿加特是队员２】\x01",        # 0
            "【◇队伍变成１人之前，提妲是队员２】\x01",          # 1
            "【◇队伍变成１人之前，奥利维尔是队员２】\x01",      # 2
            "【◇队伍变成１人之前，科洛丝是队员２】\x01",        # 3
            "【◇队伍变成１人之前，金是队员２】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F4C"),
        (1, "loc_1F52"),
        (2, "loc_1F58"),
        (3, "loc_1F5E"),
        (4, "loc_1F64"),
        (SWITCH_DEFAULT, "loc_1F6A"),
    )


    label("loc_1F4C")

    OP_A2(0x1829)
    Jump("loc_1F6A")

    label("loc_1F52")

    OP_A2(0x182A)
    Jump("loc_1F6A")

    label("loc_1F58")

    OP_A2(0x182B)
    Jump("loc_1F6A")

    label("loc_1F5E")

    OP_A2(0x182C)
    Jump("loc_1F6A")

    label("loc_1F64")

    OP_A2(0x182D)
    Jump("loc_1F6A")

    label("loc_1F6A")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇队伍变成１人之前，阿加特是队员３】\x01",        # 0
            "【◇队伍变成１人之前，提妲是队员３】\x01",          # 1
            "【◇队伍变成１人之前，奥利维尔是队员３】\x01",      # 2
            "【◇队伍变成１人之前，科洛丝是队员３】\x01",        # 3
            "【◇队伍变成１人之前，金是队员３】\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2069"),
        (1, "loc_206F"),
        (2, "loc_2075"),
        (3, "loc_207B"),
        (4, "loc_2081"),
        (SWITCH_DEFAULT, "loc_2087"),
    )


    label("loc_2069")

    OP_A2(0x182E)
    Jump("loc_2087")

    label("loc_206F")

    OP_A2(0x182F)
    Jump("loc_2087")

    label("loc_2075")

    OP_A2(0x1830)
    Jump("loc_2087")

    label("loc_207B")

    OP_A2(0x1831)
    Jump("loc_2087")

    label("loc_2081")

    OP_A2(0x1832)
    Jump("loc_2087")

    label("loc_2087")

    AddParty(0x2, 0xF7, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 1)), scpexpr(EXPR_END)), "loc_2099")
    AddParty(0x5, 0xF8, 0xFF)
    Jump("loc_20CE")

    label("loc_2099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 2)), scpexpr(EXPR_END)), "loc_20A7")
    AddParty(0x6, 0xF8, 0xFF)
    Jump("loc_20CE")

    label("loc_20A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 3)), scpexpr(EXPR_END)), "loc_20B5")
    AddParty(0x3, 0xF8, 0xFF)
    Jump("loc_20CE")

    label("loc_20B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 4)), scpexpr(EXPR_END)), "loc_20C3")
    AddParty(0x4, 0xF8, 0xFF)
    Jump("loc_20CE")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 5)), scpexpr(EXPR_END)), "loc_20CE")
    AddParty(0x7, 0xF8, 0xFF)

    label("loc_20CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 6)), scpexpr(EXPR_END)), "loc_20DC")
    AddParty(0x5, 0xF9, 0xFF)
    Jump("loc_2111")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 7)), scpexpr(EXPR_END)), "loc_20EA")
    AddParty(0x6, 0xF9, 0xFF)
    Jump("loc_2111")

    label("loc_20EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 0)), scpexpr(EXPR_END)), "loc_20F8")
    AddParty(0x3, 0xF9, 0xFF)
    Jump("loc_2111")

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 1)), scpexpr(EXPR_END)), "loc_2106")
    AddParty(0x4, 0xF9, 0xFF)
    Jump("loc_2111")

    label("loc_2106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 2)), scpexpr(EXPR_END)), "loc_2111")
    AddParty(0x7, 0xF9, 0xFF)

    label("loc_2111")

    OP_6D(-46680, 20, 12540, 0)
    OP_67(0, 6420, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    SetChrPos(0x101, -47720, 20, 12910, 0)
    SetChrPos(0x103, -46230, -20, 13170, 270)
    SetChrPos(0xF8, -47480, -60, 11470, 0)
    SetChrPos(0xF9, -46420, -60, 11450, 0)

    NpcTalk(    #45
        0x103,
        "女性的声音",
        (
            "#2P艾丝蒂尔！\x01",
            "振作一点啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1007F#6P嗯……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_21F4"),
        (6, "loc_21FC"),
        (3, "loc_2204"),
        (4, "loc_220C"),
        (7, "loc_2214"),
        (SWITCH_DEFAULT, "loc_221C"),
    )


    label("loc_21F4")

    SetChrChipByIndex(0xF8, 4)
    Jump("loc_221C")

    label("loc_21FC")

    SetChrChipByIndex(0xF8, 5)
    Jump("loc_221C")

    label("loc_2204")

    SetChrChipByIndex(0xF8, 6)
    Jump("loc_221C")

    label("loc_220C")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_221C")

    label("loc_2214")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_221C")

    label("loc_221C")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_2239"),
        (6, "loc_2241"),
        (3, "loc_2249"),
        (4, "loc_2251"),
        (7, "loc_2259"),
        (SWITCH_DEFAULT, "loc_2261"),
    )


    label("loc_2239")

    SetChrChipByIndex(0xF9, 4)
    Jump("loc_2261")

    label("loc_2241")

    SetChrChipByIndex(0xF9, 5)
    Jump("loc_2261")

    label("loc_2249")

    SetChrChipByIndex(0xF9, 6)
    Jump("loc_2261")

    label("loc_2251")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_2261")

    label("loc_2259")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_2261")

    label("loc_2261")

    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #47
        0x101,
        "#1026F#6P啊……雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#023F#2P艾丝蒂尔！？\x02\x03",

            "#524F太好了……\x01",
            "你终于醒过来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1025F#6P啊……嗯……\x02\x03",

            "我好像…\x01",
            "做了一个好长好长的梦……\x02",
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

    ChrTalk(    #50
        0x101,
        (
            "#1017F#5P是吗……\x02\x03",

            "……多亏了它……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x101,
        (
            "#1005F#5P你们两个！！\x01",
            "美梦已经结束了！\x02\x03",

            "赶快回到现实来！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#023F#2P艾、艾丝蒂尔！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2407")

    ChrTalk(    #53
        0x107,
        "#561F嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_248E")

    label("loc_2407")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2429")

    ChrTalk(    #54
        0x106,
        "#056F厄……\x02",
    )

    CloseMessageWindow()
    Jump("loc_248E")

    label("loc_2429")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244D")

    ChrTalk(    #55
        0x104,
        "#034F嗯啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_248E")

    label("loc_244D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_246F")

    ChrTalk(    #56
        0x105,
        "#049F啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_248E")

    label("loc_246F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_248E")

    ChrTalk(    #57
        0x108,
        "#572F呜……\x02",
    )

    CloseMessageWindow()

    label("loc_248E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2510")

    ChrTalk(    #58
        0x107,
        "#064F啊……艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2595")

    label("loc_2510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253E")

    ChrTalk(    #59
        0x105,
        "#044F啊……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2595")

    label("loc_253E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_256E")

    ChrTalk(    #60
        0x104,
        "#033F哎呀……艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2595")

    label("loc_256E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(    #61
        0x106,
        "#052F艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    label("loc_2595")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CE")

    ChrTalk(    #62
        0x108,
        (
            "#572F是吗……\x01",
            "原来被困在梦中了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2674")

    label("loc_25CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_260B")

    ChrTalk(    #63
        0x106,
        (
            "#552F是吗……\x01",
            "原来刚才的一切都是梦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2674")

    label("loc_260B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2642")

    ChrTalk(    #64
        0x104,
        (
            "#032F嗯……\x01",
            "原来被困在梦中了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2674")

    label("loc_2642")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2674")

    ChrTalk(    #65
        0x105,
        (
            "#049F是吗……\x01",
            "原来…是梦啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2674")


    ChrTalk(    #66
        0x101,
        (
            "#1006F#5P太好了……\x01",
            "大家都醒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x103,
        (
            "#524F#2P呵……\x01",
            "都是被艾丝蒂尔你吓醒的啊。\x02\x03",

            "不但可以凭自己的力量醒来，\x01",
            "竟然还能把别人也叫醒呢。\x02\x03",

            "#026F那么，接下来……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    Sleep(500)

    ChrTalk(    #68
        0x103,
        (
            "#024F#2P#3S你在这里吧？快现身吧！\x01",
            "露茜奥拉姐姐！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #69
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #70
        (
            "\x07\x05呵呵……\x01",
            "终于被认出来了啊。\x02",
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

    def lambda_27EF():
        OP_6D(-45560, -10, 16980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27EF)

    def lambda_2807():
        OP_67(0, 5240, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2807)

    def lambda_281F():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_281F)

    def lambda_282F():
        OP_6E(325, 3000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_282F)

    def lambda_283F():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_283F)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xC, -46320, 70, 19130, 180)

    def lambda_2881():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_2881)
    OP_22(0x99, 0x0, 0x64)
    OP_43(0xA, 0x1, 0x0, 0xA)
    OP_43(0xB, 0x1, 0x0, 0xB)
    OP_82(0x0, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E1")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_291F")

    label("loc_28E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2908")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_291F")

    label("loc_2908")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_291F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2946")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2984")

    label("loc_2946")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296D")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2984")

    label("loc_296D")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2984")

    Sleep(1000)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #71
        0x101,
        "#1020F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        "#022F#2P……果然……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #73
        0xC,
        "黑衣女子",
        (
            "#240F好久不见了啊，雪拉扎德。\x02\x03",

            "已经有８年了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#522F#2P嗯……是啊。\x02\x03",

            "真没想到姐姐你竟然…\x01",
            "会做出这样的事情来……\x02\x03",

            "#022F你究竟……为什么要这么做！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 0, 500)
    Sleep(500)

    ChrTalk(    #75
        0x101,
        (
            "#1020F#6P等、等一下！\x02\x03",

            "这个人……\x01",
            "和雪拉姐是旧识吗！？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0xC,
        "黑衣女子",
        (
            "#241F呵呵……\x01",
            "真是薄情啊，小鬼头。\x02\x03",

            "你我之间可也是\x01",
            "见过好几次面的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1004F#6P哎？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0xC,
        "黑衣女子",
        (
            "#241F和你一起玩塔罗牌\x01",
            "的幻术师姐姐……\x02\x03",

            "你已经不记得了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1020F#6P！！！\x02",
    )

    CloseMessageWindow()
    OP_AD(0x24007D, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #80
        0x101,
        (
            "#1020F#6P你、你就是当时的……\x02\x03",

            "露……\x01",
            "露茜奥拉姐姐！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0xC,
        "黑衣女子",
        "#241F呵呵～没错。\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS117._CH")
    OP_C6(0x0, 0x0, 125000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("黑衣女子")

    AnonymousTalk(    #82
        (
            "\x07\x00#241F执行者ＮＯ．Ⅵ。\x01",
            "『幻惑之铃』露茜奥拉。\x02\x03",

            "这就是我现在的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    Sleep(250)

    ChrTalk(    #83
        0x101,
        "#1020F#6P为、为什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "#240F呵呵，雪拉扎德。\x01",
            "你似乎早就猜出是我了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x103,
        (
            "#026F#2P驱铃之幻术……\x01",
            "可是姐姐的拿手绝活啊。\x02\x03",

            "#022F不过洛连特产生的浓雾\x01",
            "应该不是用幻术做出的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xC,
        (
            "#241F呵呵，当然。\x02\x03",

            "那个是为了这次的实验\x01",
            "而用『福音』引起的现象哦。\x02\x03",

            "能顺利干涉到人们的梦境，\x01",
            "这些雾可是起到了重要的触媒作用哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#023F#2P触媒……\x02\x03",

            "#024F难道说『福音』\x01",
            "连人的精神也可以干扰到吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "#240F呵呵～似乎就是这样哦。\x02\x03",

            "我的铃声只是诱导……\x02\x03",

            "诱导大家进入远比幻术\x01",
            "还要真实的梦境。\x02\x03",

            "#244F在梦境里，大家没有痛苦，\x01",
            "没有悲伤，只有幸福和快乐。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F1C")

    ChrTalk(    #89
        0x107,
        "#063F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_2F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4A")

    ChrTalk(    #90
        0x106,
        (
            "#552F可恶……\x01",
            "竟敢耍我……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F80")

    ChrTalk(    #91
        0x104,
        (
            "#032F哎呀呀……\x01",
            "真是低级的嗜好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F80")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(    #92
        0x105,
        "#043F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD8")

    ChrTalk(    #93
        0x108,
        "#072F嗯，原来如此啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2FD8")


    ChrTalk(    #94
        0x103,
        "#522F#2P……呜………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1002F#6P那个，露茜奥拉……姐姐。\x02\x03",

            "为什么『结社』\x01",
            "要一直干这种事？\x02\x03",

            "不断进行这些实验，\x01",
            "到底是为了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "#240F我身为结社的『执行者』，\x01",
            "只会按照『使徒』的指示而行动。\x02\x03",

            "也就是说，我只不过是\x01",
            "这次计划的协力者而已。\x02\x03",

            "详细情况\x01",
            "你们就去问教授和莱维吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1002F#6P教授、莱维……\x02\x03",

            "这两个名字我们已经听过好几次了，\x01",
            "他们究竟是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "#241F时候一到，你们自然就知道了。\x02\x03",

            "顺便一提，他们两个\x01",
            "好像都认识你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1004F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x103,
        (
            "#522F#2P…………………………………\x02\x03",

            "……露茜奥拉姐姐。\x01",
            "你能听我说几句话吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        "#243F啊……是什么呢？\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(    #102
        0x103,
        (
            "#524F#2P在一开始，我并没有打算\x01",
            "定居在利贝尔……\x02\x03",

            "只是想在姐姐回来之前\x01",
            "暂时待在这里。\x02\x03",

            "#026F可是，８年时间转眼就过去了。\x02\x03",

            "现在的我，在这里已经有了朋友和同伴，\x01",
            "有了相当于家人一般的人们，\x01",
            "也有了引以为荣的工作。\x02\x03",

            "#022F我早已经……不再是哈维剧团里\x01",
            "那个跳舞的小孩雪拉扎德了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1026F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xC,
        "#242F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x103,
        "#026F#2P这里是我新的家乡……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 16)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #106
        0x103,
        (
            "#024F#2P如果有人想破坏这里的话，\x01",
            "就算是姐姐你我也不会原谅的！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        (
            "#244F呵呵……很好。\x02\x03",

            "#241F对你们来说，\x01",
            "『结社』实在是太过强大了，\x02\x03",

            "想要与之抗衡，就要拿出全部的力量。\x02",
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

    ChrTalk(    #108
        0x101,
        "#1004F#6P啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        "#023F#2P姐姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "#241F呵呵……\x01",
            "不久之后我们还会再见面的。\x02\x03",

            "想叙旧的话到时候再继续吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11E, 0x0, 0x64)

    def lambda_3582():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3582)

    def lambda_3594():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3594)

    def lambda_35A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_35A6)
    Sleep(500)

    def lambda_35BD():
        OP_6D(-45830, 10, 17150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35BD)

    def lambda_35D5():
        OP_6C(33000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35D5)
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

    ChrTalk(    #111
        0x103,
        "#522F#5P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #112
        0x101,
        "#1026F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #113
        0x103,
        "#025F#6P……呼，真是的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(500)

    ChrTalk(    #114
        0x103,
        (
            "#524F#5P虽然被她逃走了……\x01",
            "但事件至此为止应该也算是解决了吧。\x02\x03",

            "昏睡中的人们\x01",
            "应该马上都会醒来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0100   ._SN", 119, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1E1D end

    def Function_9_370B(): pass

    label("Function_9_370B")

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

    # Function_9_370B end

    def Function_10_3757(): pass

    label("Function_10_3757")

    SetChrSubChip(0xA, 0)
    SetChrPos(0xA, -46320, 70, 19130, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_377E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_377E)
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

    # Function_10_3757 end

    def Function_11_3840(): pass

    label("Function_11_3840")

    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, -46320, 70, 19130, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3867():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_3867)
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

    # Function_11_3840 end

    def Function_12_3929(): pass

    label("Function_12_3929")

    SetChrSubChip(0xA, 0)
    SetChrPos(0xA, -46320, 70, 19130, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_91(0xA, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0x64, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)

    label("loc_399F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39D3")
    OP_91(0xA, 0x96, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xA, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_399F")

    label("loc_39D3")

    Return()

    # Function_12_3929 end

    def Function_13_39D4(): pass

    label("Function_13_39D4")

    SetChrSubChip(0xB, 0)
    SetChrPos(0xB, -46320, 70, 19130, 180)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_91(0xB, 0xFFFFFFCE, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x32, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0xFFFFFF9C, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x64, 0x0, 0x0, 0x12C, 0x0)

    label("loc_3A4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A7E")
    OP_91(0xB, 0xFFFFFF6A, 0x0, 0x0, 0x12C, 0x0)
    OP_91(0xB, 0x96, 0x0, 0x0, 0x12C, 0x0)
    Jump("loc_3A4A")

    label("loc_3A7E")

    Return()

    # Function_13_39D4 end

    def Function_14_3A7F(): pass

    label("Function_14_3A7F")

    EventBegin(0x1)

    ChrTalk(    #115
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_3AAB():
        OP_6D(55440, 360, 7980, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3AAB)

    def lambda_3AC3():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3AC3)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #116
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFB")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x3, 0xD174, 0x17C, 0x2044, 0x5A, 0xDEC6, 0xFFFFFC18, 0x1E32)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_3BF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BEF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BEC")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x40)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #117
        (
            "\x07\x05把在神秘森林中发现钓鱼场的事情\x01",
            "已经记录在游击士手册上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_3BEC")

    Jump("loc_3BF5")

    label("loc_3BEF")

    OP_28(0x73, 0x1, 0x4000)

    label("loc_3BF5")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_3C0A")

    label("loc_3BFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C0A")
    EventEnd(0x1)

    label("loc_3C0A")

    Return()

    # Function_14_3A7F end

    def Function_15_3C0B(): pass

    label("Function_15_3C0B")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C88"),
        (1, "loc_3C8E"),
        (SWITCH_DEFAULT, "loc_3C94"),
    )


    label("loc_3C88")

    OP_A2(0x1200)
    Jump("loc_3C94")

    label("loc_3C8E")

    OP_A2(0x1201)
    Jump("loc_3C94")

    label("loc_3C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3CA2")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3CA6")

    label("loc_3CA2")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3CA6")

    Return()

    # Function_15_3C0B end

    def Function_16_3CA7(): pass

    label("Function_16_3CA7")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_16_3CA7 end

    SaveToFile()

Try(main)
