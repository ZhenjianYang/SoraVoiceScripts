from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5504   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5504.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '雪拉扎德',                             # 9
        '鸡首普洛斯',                           # 10
        '鸡首普洛斯',                           # 11
        '鸡首普洛斯',                           # 12
        '鸡首普洛斯',                           # 13
        '封印石⑩',                             # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT07/CH00120 ._CH',             # 00
        'ED6_DT07/CH00121 ._CH',             # 01
        'ED6_DT29/CH14740 ._CH',             # 02
        'ED6_DT29/CH14741 ._CH',             # 03
        'ED6_DT29/CH14540 ._CH',             # 04
        'ED6_DT29/CH14541 ._CH',             # 05
        'ED6_DT29/CH15110 ._CH',             # 06
        'ED6_DT29/CH15111 ._CH',             # 07
        'ED6_DT29/CH14530 ._CH',             # 08
        'ED6_DT29/CH14531 ._CH',             # 09
        'ED6_DT26/CH20621 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00120P._CP',             # 00
        'ED6_DT07/CH00121P._CP',             # 01
        'ED6_DT29/CH14740P._CP',             # 02
        'ED6_DT29/CH14741P._CP',             # 03
        'ED6_DT29/CH14540P._CP',             # 04
        'ED6_DT29/CH14541P._CP',             # 05
        'ED6_DT29/CH15110P._CP',             # 06
        'ED6_DT29/CH15111P._CP',             # 07
        'ED6_DT29/CH14530P._CP',             # 08
        'ED6_DT29/CH14531P._CP',             # 09
        'ED6_DT26/CH20621P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 22330,
        Z                   = 0,
        Y                   = 17900,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x197,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -22340,
        Y                   = -1000,
        Z                   = -10060,
        Range               = 4000,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = -4390,
        TriggerZ            = 0,
        TriggerY            = 33260,
        TriggerRange        = 1000,
        ActorX              = -4390,
        ActorZ              = 2000,
        ActorY              = 33260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22270,
        TriggerZ            = 0,
        TriggerY            = 34210,
        TriggerRange        = 1000,
        ActorX              = 22270,
        ActorZ              = 1000,
        ActorY              = 34210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_284",          # 02, 2
        "Function_3_295",          # 03, 3
        "Function_4_C41",          # 04, 4
        "Function_5_121C",         # 05, 5
        "Function_6_124C",         # 06, 6
        "Function_7_1277",         # 07, 7
        "Function_8_12A7",         # 08, 8
        "Function_9_12D7",         # 09, 9
        "Function_10_1329",        # 0A, 10
        "Function_11_138E",        # 0B, 11
        "Function_12_13F3",        # 0C, 12
        "Function_13_1458",        # 0D, 13
        "Function_14_14BD",        # 0E, 14
        "Function_15_1755",        # 0F, 15
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Return()

    # Function_0_246 end

    def Function_1_247(): pass

    label("Function_1_247")

    OP_16(0x2, 0xFA0, 0xFFFDF878, 0xFFFE6DA8, 0x2300A1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    OP_82(0x91, 0x0)
    OP_82(0x92, 0x0)
    OP_82(0x94, 0x0)

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x537, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C")
    OP_6F(0x0, 0)
    Jump("loc_283")

    label("loc_27C")

    OP_6F(0x0, 60)

    label("loc_283")

    Return()

    # Function_1_247 end

    def Function_2_284(): pass

    label("Function_2_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 1)), scpexpr(EXPR_END)), "loc_28C")
    Return()

    label("loc_28C")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_284 end

    def Function_3_295(): pass

    label("Function_3_295")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_340")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_368")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_390")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A7")

    label("loc_390")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_3F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_436")

    label("loc_41F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_436")

    Sleep(1000)

    def lambda_441():
        OP_6D(-28950, 0, -18620, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_441)

    def lambda_459():
        OP_67(0, 5880, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_459)

    def lambda_471():
        OP_6B(3330, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_471)

    def lambda_481():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_481)

    def lambda_491():
        OP_6E(250, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_491)

    def lambda_4A1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4A1)

    def lambda_4AF():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_4AF)

    def lambda_4BD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_4BD)

    def lambda_4CB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_4CB)
    WaitChrThread(0xEE, 0x2)
    SetChrPos(0xEE, -23720, 0, -7770, 180)
    SetChrPos(0xEF, -22280, 0, -7300, 180)
    SetChrPos(0xF0, -23740, 0, -5960, 180)
    SetChrPos(0xF1, -22500, 0, -5310, 180)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -28030, 100, -18770, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, -25670, 0, -21170, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, -28610, 0, -21010, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -31000, 0, -18930, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFF, -30970, 0, -16520, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_662():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_662)
    OP_22(0x85, 0x1, 0x64)

    def lambda_677():

        label("loc_677")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_677")

    QueueWorkItem2(0x109, 0, lambda_677)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -28030, -3000, -18770, 45)
    SetChrSubChip(0x10, 0)
    OP_43(0x10, 0x0, 0x0, 0x9)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -25670, -3000, -21170, 45)
    OP_43(0x11, 0x0, 0x0, 0xA)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -28610, -3000, -21010, 45)
    OP_43(0x12, 0x0, 0x0, 0xB)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -31000, -3000, -18930, 45)
    OP_43(0x13, 0x0, 0x0, 0xC)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -30970, -3000, -16520, 45)
    OP_43(0x14, 0x0, 0x0, 0xD)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    OP_1D(0xC4)
    OP_44(0x109, 0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\mp250_00.eff")
    Sleep(500)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    ClearMapFlags(0x10)
    OP_6D(-26280, 0, -16090, 0)
    OP_67(0, 6630, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(269000, 0)
    OP_6E(278, 0)
    SetChrPos(0xEE, -20800, 0, -7830, 180)
    SetChrPos(0xEF, -19170, 60, -8210, 180)
    SetChrPos(0xF0, -20690, 0, -5830, 180)
    SetChrPos(0xF1, -19130, 430, -7000, 180)
    OP_43(0x109, 0x0, 0x0, 0x5)
    OP_43(0x102, 0x0, 0x0, 0x6)
    OP_43(0xF0, 0x0, 0x0, 0x7)
    OP_43(0xF1, 0x0, 0x0, 0x8)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #0
        0x102,
        "#1506F#6P雪拉姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "#529F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A6")

    ChrTalk(    #2
        0x104,
        "#1543F#12P哦哦……是雪拉君！\x02",
    )

    CloseMessageWindow()

    label("loc_8A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(    #3
        0x10A,
        "#1317F#4P雪拉前辈……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D")

    label("loc_8DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90F")

    ChrTalk(    #4
        0x108,
        "#072F#4P雪拉扎德……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D")

    label("loc_90F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_947")

    ChrTalk(    #5
        0x107,
        "#065F#4P雪、雪拉姐姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D")

    label("loc_947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97D")

    ChrTalk(    #6
        0x105,
        "#1163F#4P雪拉扎德小姐……！\x02",
    )

    CloseMessageWindow()

    label("loc_97D")


    ChrTalk(    #7
        0x109,
        (
            "#1065F#12P这次是这个大姐啊……\x02\x03",

            "#1063F不愧是协会的训练场，\x01",
            "出现的人都是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1502F#6P……想办法打败她\x01",
            "回收封印石吧。\x02\x03",

            "那样应该就能解放\x01",
            "真正的雪拉姐姐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1069F#12P啊啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A78():
        OP_6D(-27040, 0, -15960, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A78)

    def lambda_A90():
        OP_67(0, 6630, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A90)

    def lambda_AA8():
        OP_6B(2640, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AA8)

    def lambda_AB8():
        OP_6E(264, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AB8)

    def lambda_AC8():
        OP_8F(0xFE, 0xFFFF9B56, 0x0, 0xFFFFC3F6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC8)
    SetChrChipByIndex(0x10, 1)

    def lambda_AE8():
        OP_8F(0xFE, 0xFFFF9944, 0x0, 0xFFFFBF00, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_AE8)
    Sleep(10)
    SetChrChipByIndex(0x14, 9)

    def lambda_B0D():

        label("loc_B0D")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_B0D")

    QueueWorkItem2(0x14, 3, lambda_B0D)

    def lambda_B20():
        OP_8F(0xFE, 0xFFFF9E76, 0x0, 0xFFFFC748, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_B20)

    def lambda_B3B():
        OP_8F(0xFE, 0xFFFF9F66, 0x0, 0xFFFFC07C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B3B)
    Sleep(10)
    SetChrChipByIndex(0x12, 9)

    def lambda_B60():

        label("loc_B60")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_B60")

    QueueWorkItem2(0x12, 3, lambda_B60)

    def lambda_B73():
        OP_8F(0xFE, 0xFFFFA376, 0x0, 0xFFFFC310, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B73)

    def lambda_B8E():
        OP_8F(0xFE, 0xFFFF9B56, 0x0, 0xFFFFC3F6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_B8E)
    Sleep(10)
    SetChrChipByIndex(0x13, 9)

    def lambda_BB3():

        label("loc_BB3")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_BB3")

    QueueWorkItem2(0x13, 3, lambda_BB3)

    def lambda_BC6():
        OP_8F(0xFE, 0xFFFFA042, 0x0, 0xFFFFC586, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_BC6)

    def lambda_BE1():
        OP_8F(0xFE, 0xFFFF9F66, 0x0, 0xFFFFC07C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_BE1)
    Sleep(10)
    SetChrChipByIndex(0x11, 9)

    def lambda_C06():

        label("loc_C06")

        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        OP_48()
        Jump("loc_C06")

    QueueWorkItem2(0x11, 3, lambda_C06)

    def lambda_C19():
        OP_8F(0xFE, 0xFFFFA506, 0x0, 0xFFFFC11C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C19)
    WaitChrThread(0x109, 0x1)
    Battle(0x1A4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_295 end

    def Function_4_C41(): pass

    label("Function_4_C41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    OP_E0(238, 0x4B, 0x2)
    OP_E0(238, 0x4C, 0x3)
    OP_E0(239, 0x4D, 0x2)
    OP_E0(239, 0x4E, 0x3)
    OP_E0(240, 0x4F, 0x2)
    OP_E0(240, 0x50, 0x3)
    OP_E0(241, 0x51, 0x2)
    OP_E0(241, 0x52, 0x3)
    SetChrPos(0xEE, -24440, 0, -16610, 225)
    SetChrPos(0xEF, -23630, 0, -17790, 225)
    SetChrPos(0xF0, -22810, 0, -15600, 225)
    SetChrPos(0xF1, -21900, 0, -17040, 225)
    SetChrChipByIndex(0xEE, 11)
    SetChrSubChip(0xEE, 0)
    SetChrChipByIndex(0xEF, 13)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 15)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 17)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-27690, 0, -18130, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(269000, 0)
    OP_6E(286, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -27200, 1200, -19420, 0)
    PlayEffect(0x7, 0x7, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_E9A():
        OP_6D(-27740, 0, -18560, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E9A)

    def lambda_EB2():
        OP_67(0, 4970, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_EB2)

    def lambda_ECA():
        OP_6B(3100, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_ECA)

    def lambda_EDA():
        OP_6E(286, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EDA)
    OP_8F(0x109, 0xFFFF9930, 0x0, 0xFFFFB618, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x15, 0xFFFF975A, 0x4E2, 0xFFFFB51E, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x5B\x03\x07\x00。\x02",
    )

    Jump("loc_F77")

    label("loc_F77")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35B, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #11
        0x109,
        "#1078F#5P好……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1513F#6P这样……\x01",
            "就能解放雪拉姐姐了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1038")

    ChrTalk(    #13
        0x10B,
        (
            "#413F#12P嗯……\x01",
            "那个使鞭子的大姐吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1099")

    ChrTalk(    #14
        0x104,
        (
            "#1541F#12P呼……\x01",
            "久违的相会吗。\x02\x03",

            "#1540F那么，\x01",
            "赶快回据点吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10EB")

    label("loc_1099")

    OP_8C(0x109, 45, 400)
    Sleep(300)

    ChrTalk(    #15
        0x109,
        (
            "#1075F#5P嗯，没错的。\x02\x03",

            "#1060F好……\x01",
            "赶快回据点吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1147")

    ChrTalk(    #16
        0x10A,
        (
            "#811F#12P呵呵，真期待啊。\x02\x03",

            "#1310F有前辈在\x01",
            "就能以一当十了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1147")

    OP_A2(0x2909)
    OP_28(0x33, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-26440, 0, -18550, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -26440, 0, -18550, 45)
    SetChrPos(0x1, -26440, 0, -18550, 45)
    SetChrPos(0x2, -26440, 0, -18550, 45)
    SetChrPos(0x3, -26440, 0, -18550, 45)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_4_C41 end

    def Function_5_121C(): pass

    label("Function_5_121C")

    Sleep(150)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA1BE, 0x0, 0xFFFFCA36, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_121C end

    def Function_6_124C(): pass

    label("Function_6_124C")

    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA6D2, 0x0, 0xFFFFC626, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_124C end

    def Function_7_1277(): pass

    label("Function_7_1277")

    Sleep(200)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFA7A4, 0x0, 0xFFFFCEBE, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_7_1277 end

    def Function_8_12A7(): pass

    label("Function_8_12A7")

    Sleep(100)
    OP_8C(0xFE, 225, 0)
    OP_8F(0xFE, 0xFFFFAC2C, 0x0, 0xFFFFCAD6, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_12A7 end

    def Function_9_12D7(): pass

    label("Function_9_12D7")

    PlayEffect(0x1, 0xFF, 0xFF, -28030, 100, -18770, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_12D7 end

    def Function_10_1329(): pass

    label("Function_10_1329")

    PlayEffect(0x1, 0xFF, 0xFF, -25670, 0, -21170, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1364():

        label("loc_1364")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1364")

    QueueWorkItem2(0xFE, 3, lambda_1364)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1329 end

    def Function_11_138E(): pass

    label("Function_11_138E")

    PlayEffect(0x1, 0xFF, 0xFF, -28610, 0, -21010, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_13C9():

        label("loc_13C9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13C9")

    QueueWorkItem2(0xFE, 3, lambda_13C9)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_138E end

    def Function_12_13F3(): pass

    label("Function_12_13F3")

    PlayEffect(0x1, 0xFF, 0xFF, -31000, 0, -18930, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_142E():

        label("loc_142E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_142E")

    QueueWorkItem2(0xFE, 3, lambda_142E)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_13F3 end

    def Function_13_1458(): pass

    label("Function_13_1458")

    PlayEffect(0x1, 0xFF, 0xFF, -30970, 0, -16520, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_1493():

        label("loc_1493")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1493")

    QueueWorkItem2(0xFE, 3, lambda_1493)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_1458 end

    def Function_14_14BD(): pass

    label("Function_14_14BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158C")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x91, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(3328)
    Sleep(500)
    Jump("loc_158F")

    label("loc_158C")

    TalkBegin(0xFF)

    label("loc_158F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #17
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_15B9")

    label("loc_15B9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1724")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_161E")

    label("loc_161E")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_163B"),
        (1, "loc_16B6"),
        (2, "loc_16E5"),
        (SWITCH_DEFAULT, "loc_1714"),
    )


    label("loc_163B")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE7)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1721")

    label("loc_16B6")

    OP_A9(0x20)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_16E2")

    label("loc_16E2")

    Jump("loc_1721")

    label("loc_16E5")

    OP_A9(0x7)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #19
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_1711")

    label("loc_1711")

    Jump("loc_1721")

    label("loc_1714")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1721")

    label("loc_1721")

    Jump("loc_15CC")

    label("loc_1724")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1751")
    OP_A2(0x2590)
    EventEnd(0x1)
    Jump("loc_1754")

    label("loc_1751")

    TalkEnd(0xFF)

    label("loc_1754")

    Return()

    # Function_14_14BD end

    def Function_15_1755(): pass

    label("Function_15_1755")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x537, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1836")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x41B, 1)"), scpexpr(EXPR_END)), "loc_17C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x1B\x04\x07\x00。\x02",
    )

    Jump("loc_17AC")

    label("loc_17AC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B8)
    Jump("loc_1833")

    label("loc_17C7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "宝箱里装有\x1F\x1B\x04\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x1B\x04\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1814")

    label("loc_1814")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_1833")

    Jump("loc_1867")

    label("loc_1836")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1867")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1755 end

    SaveToFile()

Try(main)
