from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5615   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5615.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        '克鲁茨',                               # 9
        '猎兵克鲁茨',                           # 10
        '猎兵克鲁茨',                           # 11
        '',                                     # 12
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
        'ED6_DT29/CH14950 ._CH',             # 00
        'ED6_DT29/CH14951 ._CH',             # 01
        'ED6_DT29/CH14960 ._CH',             # 02
        'ED6_DT29/CH14961 ._CH',             # 03
        'ED6_DT29/CH14961 ._CH',             # 04
        'ED6_DT07/CH01620 ._CH',             # 05
        'ED6_DT07/CH00410 ._CH',             # 06
        'ED6_DT07/CH00411 ._CH',             # 07
        'ED6_DT07/CH00414 ._CH',             # 08
        'ED6_DT07/CH00415 ._CH',             # 09
        'ED6_DT27/CH04630 ._CH',             # 0A
        'ED6_DT27/CH04631 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14950P._CP',             # 00
        'ED6_DT29/CH14951P._CP',             # 01
        'ED6_DT29/CH14960P._CP',             # 02
        'ED6_DT29/CH14961P._CP',             # 03
        'ED6_DT29/CH14961P._CP',             # 04
        'ED6_DT07/CH01620P._CP',             # 05
        'ED6_DT07/CH00410P._CP',             # 06
        'ED6_DT07/CH00411P._CP',             # 07
        'ED6_DT07/CH00414P._CP',             # 08
        'ED6_DT07/CH00415P._CP',             # 09
        'ED6_DT27/CH04630P._CP',             # 0A
        'ED6_DT27/CH04631P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -142040,
        TriggerZ            = 0,
        TriggerY            = -40,
        TriggerRange        = 800,
        ActorX              = -142040,
        ActorZ              = 1000,
        ActorY              = -40,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18E",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1B1",          # 02, 2
        "Function_3_1BA",          # 03, 3
        "Function_4_1177",         # 04, 4
        "Function_5_11CC",         # 05, 5
        "Function_6_1221",         # 06, 6
        "Function_7_1FFE",         # 07, 7
        "Function_8_20BD",         # 08, 8
    )


    def Function_0_18E(): pass

    label("Function_0_18E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6")
    Event(0, 2)

    label("loc_1A6")

    Return()

    # Function_0_18E end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    OP_74(0x0, 0x0, 0x0)
    Return()

    # Function_1_1A7 end

    def Function_2_1B1(): pass

    label("Function_2_1B1")

    Call(0, 3)
    Call(0, 6)
    Return()

    # Function_2_1B1 end

    def Function_3_1BA(): pass

    label("Function_3_1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4C, 0x2)
    OP_E0(238, 0x4D, 0x3)
    OP_E0(239, 0x4E, 0x2)
    OP_E0(239, 0x4F, 0x3)
    OP_E0(240, 0x50, 0x2)
    OP_E0(240, 0x51, 0x3)
    OP_E0(241, 0x52, 0x2)
    OP_E0(241, 0x53, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -146020, 0, 10, 270)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -156550, 0, -830, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F")
    SetChrPos(0xEF, -156600, 0, 460, 90)
    SetChrPos(0xF0, -158050, 0, -1330, 90)
    SetChrPos(0xF1, -158000, 0, 480, 90)
    Jump("loc_324")

    label("loc_29F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3")
    SetChrPos(0xF0, -156600, 0, 460, 90)
    SetChrPos(0xEF, -158050, 0, -1330, 90)
    SetChrPos(0xF1, -158000, 0, 480, 90)
    Jump("loc_324")

    label("loc_2E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324")
    SetChrPos(0xF1, -156600, 0, 460, 90)
    SetChrPos(0xEF, -158050, 0, -1330, 90)
    SetChrPos(0xF0, -158000, 0, 480, 90)

    label("loc_324")

    OP_6D(-156350, 0, 620, 0)
    OP_67(0, 7040, -10000, 0)
    OP_6B(2240, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #0
        0x10,
        "男性的声音",
        "#3P来了吗，亚妮拉丝。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_448")

    label("loc_3E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_409")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_448")

    label("loc_409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_448")

    label("loc_431")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_448")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4DC")

    label("loc_475")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4DC")

    label("loc_49D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4DC")

    label("loc_4C5")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4DC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_509")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_570")

    label("loc_509")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_531")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_570")

    label("loc_531")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_570")

    label("loc_559")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_570")

    Sleep(1000)

    def lambda_57B():
        OP_6D(-145190, 0, 850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57B)

    def lambda_593():
        OP_67(0, 5860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_593)

    def lambda_5AB():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5AB)

    def lambda_5BB():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5BB)

    def lambda_5CB():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5CB)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #1
        0x10A,
        "#1317F#2P果、果然……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-148200, 0, 1650, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)

    def lambda_649():
        OP_8F(0xFE, 0xFFFDABA2, 0x0, 0xFFFFFBDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_649)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CF")

    def lambda_677():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_677)
    Sleep(100)

    def lambda_697():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_697)
    Sleep(100)

    def lambda_6B7():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6B7)
    Jump("loc_7A4")

    label("loc_6CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")

    def lambda_6E3():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6E3)
    Sleep(100)

    def lambda_703():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_703)
    Sleep(100)

    def lambda_723():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_723)
    Jump("loc_7A4")

    label("loc_73B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")

    def lambda_74F():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_74F)
    Sleep(100)

    def lambda_76F():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_76F)
    Sleep(100)

    def lambda_78F():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_78F)

    label("loc_7A4")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x10,
        (
            "#843F#11P嗯，连同神父先生在内，\x01",
            "有好几张以前见过的面孔。\x02\x03",

            "#845F哎呀呀，这就是所谓的缘分啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86E")

    ChrTalk(    #3
        0x103,
        (
            "#1525F#6P唉……\x01",
            "这应该是我说的才对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_86E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #4
        0x106,
        (
            "#051F#6P嘿……\x01",
            "那是我的台词啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_8AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ED")

    ChrTalk(    #5
        0x101,
        (
            "#1019F#6P那个～……\x01",
            "那是我的台词啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_8ED")


    ChrTalk(    #6
        0x109,
        (
            "#1840F#6P唔，\x01",
            "这肯定不会是女神的旨意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_922")


    ChrTalk(    #7
        0x10A,
        (
            "#1317F#6P呃，嗯……\x02\x03",

            "#819F克鲁茨前辈\x01",
            "也要和我们战斗吗？\x02\x03",

            "那个，会不会改变主意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#844F#11P嗯，\x01",
            "在发现自己是以这种形式『存在』以后，\x01",
            "我的确尝试做过冥想之类的行动……\x02\x03",

            "#843F但看来现在的『我』\x01",
            "并不以真正意义上的\x01",
            "『自我』而存在。\x02\x03",

            "#842F因此无法脱离\x01",
            "既定的『法则』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#1316F#6P嗯，该说是太认真呢，\x01",
            "还是该说真符合克鲁茨前辈的风格……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1075F#6P哎呀哎呀，真是了不起的人。\x02\x03",

            "#1840F既然如此\x01",
            "我们也有所觉悟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#841F#11P嗯，请多指教吧。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 9)

    def lambda_B54():

        label("loc_B54")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_B54")

    QueueWorkItem2(0x10, 3, lambda_B54)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_BA3():
        OP_6D(-150200, 0, 1020, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_BA3)

    def lambda_BBB():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_BBB)

    def lambda_BD3():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_BD3)

    def lambda_BE3():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_BE3)

    def lambda_BF3():
        OP_6E(335, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BF3)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -152830, 0, 5260, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, -152330, 0, -5530, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA3")

    def lambda_C85():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_C85)
    Sleep(50)

    def lambda_C98():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_C98)
    Jump("loc_D04")

    label("loc_CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD5")

    def lambda_CB7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CB7)
    Sleep(50)

    def lambda_CCA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_CCA)
    Jump("loc_D04")

    label("loc_CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D04")

    def lambda_CE9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CE9)
    Sleep(50)

    def lambda_CFC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_CFC)

    label("loc_D04")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -152830, -3000, 5260, 180)
    SetChrPos(0x12, -152330, -3000, -5530, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_D3B():

        label("loc_D3B")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_D3B")

    QueueWorkItem2(0x109, 3, lambda_D3B)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x85)
    OP_44(0x109, 0x3)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 6)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0xEE, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC9")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E30")

    label("loc_DC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF1")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E30")

    label("loc_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E19")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E30")

    label("loc_E19")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E30")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC4")

    label("loc_E5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC4")

    label("loc_E85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC4")

    label("loc_EAD")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EC4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF1")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F58")

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F19")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F58")

    label("loc_F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F41")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F58")

    label("loc_F41")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F58")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 12)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 14)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 16)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 18)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x10A,
        (
            "#812F#6P唔，在这种距离上\x01",
            "有三个克鲁茨前辈……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        "#1069F#6P实在是不妙啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#843F#11P我的阵法是刚中带柔！\x01",
            "仿如森罗万象！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #15
        0x10,
        "#846F#11P#4S来吧，堂堂正正一决胜负！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10AB():
        OP_6D(-151200, 0, 800, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_10AB)

    def lambda_10C3():
        OP_67(0, 6000, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_10C3)

    def lambda_10DB():
        OP_6B(2350, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_10DB)

    def lambda_10EB():
        OP_6E(290, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_10EB)
    SetChrChipByIndex(0x10, 7)

    def lambda_1100():
        OP_8F(0xFE, 0xFFFDAFDA, 0x0, 0xFFFFFF6A, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1100)
    SetChrChipByIndex(0x11, 11)

    def lambda_1120():
        OP_8F(0xFE, 0xFFFDA7E2, 0x0, 0xDC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1120)
    SetChrChipByIndex(0x12, 11)

    def lambda_1140():
        OP_8F(0xFE, 0xFFFDA8DC, 0x0, 0xFFFFFAC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1140)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1BA end

    def Function_4_1177(): pass

    label("Function_4_1177")

    PlayEffect(0x1, 0x4, 0xFF, -152830, 0, 5260, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1177 end

    def Function_5_11CC(): pass

    label("Function_5_11CC")

    PlayEffect(0x1, 0x5, 0xFF, -152330, 0, -5530, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_11CC end

    def Function_6_1221(): pass

    label("Function_6_1221")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, -146020, 0, 10, 270)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0x7)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 200, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -149000, 0, -830, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133D")
    SetChrPos(0xEF, -149200, 0, 440, 90)
    SetChrPos(0xF0, -150790, 0, -1320, 90)
    SetChrPos(0xF1, -150800, 0, 370, 90)
    Jump("loc_13C2")

    label("loc_133D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1381")
    SetChrPos(0xF0, -149200, 0, 440, 90)
    SetChrPos(0xEF, -150790, 0, -1320, 90)
    SetChrPos(0xF1, -150800, 0, 370, 90)
    Jump("loc_13C2")

    label("loc_1381")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C2")
    SetChrPos(0xF1, -149200, 0, 440, 90)
    SetChrPos(0xEF, -150790, 0, -1320, 90)
    SetChrPos(0xF0, -150800, 0, 370, 90)

    label("loc_13C2")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-146860, 0, 890, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x10,
        (
            "#843F#11P呵呵，我还是很不成熟……\x01",
            "你们让我大开眼界了。\x02\x03",

            "#845F可以的话，真希望这场比试的经验\x01",
            "能残留在『我』心中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#1314F#6P前、前辈……\x01",
            "你也太认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1534")

    ChrTalk(    #18
        0x101,
        (
            "#1007F#6P比、比以前更强\x01",
            "也是理所当然的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1534")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1570")

    ChrTalk(    #19
        0x106,
        (
            "#552F#6P不会吧……\x01",
            "这个修行狂……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B5")

    ChrTalk(    #20
        0x103,
        (
            "#1534F#6P真是的……\x01",
            "让人受不了的上进心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B5")


    ChrTalk(    #21
        0x10,
        (
            "#843F#11P呵呵，\x01",
            "怎么能输给你们这些年轻人呢……\x02\x03",

            "#840F不过照这个势头……\x01",
            "你们应该有挑战『她』的资格了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1673")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DA")

    label("loc_1673")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DA")

    label("loc_169B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C3")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16DA")

    label("loc_16C3")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16DA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1707")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176E")

    label("loc_1707")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176E")

    label("loc_172F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1757")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_176E")

    label("loc_1757")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_176E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_179B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1802")

    label("loc_179B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1802")

    label("loc_17C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EB")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1802")

    label("loc_17EB")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1802")

    Sleep(1000)

    ChrTalk(    #22
        0x10A,
        "#1317F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1069F#6P等、等一下！\x01",
            "还有对手吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#843F#11P呵呵……\x01",
            "到最上层去吧。\x02\x03",

            "#841F话先说在前头……\x01",
            "『她』可是真真正正的强者。\x02\x03",

            "那样年轻，作为\x01",
            "武术家却已大有所为了。\x02\x03",

            "如果没做好觉悟\x01",
            "还是不要去挑战比较安全。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 250, -700, 0, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_1973():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1973)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(500)
    OP_6D(-148370, 0, 960, 1500)
    Sleep(500)

    ChrTalk(    #25
        0x10A,
        "#1317F#5P那个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B73")

    ChrTalk(    #26
        0x109,
        (
            "#1068F#6P喂喂……\x01",
            "这上面还有杀手锏啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A98")

    ChrTalk(    #27
        0x101,
        (
            "#1007F#6P我、我好像有一种\x01",
            "很不好的预感。\x02\x03",

            "#1019F是『她』又是『武术家』的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B70")

    label("loc_1A98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B07")

    ChrTalk(    #28
        0x103,
        (
            "#1525F#6P呼……\x01",
            "有种很不好的预感呢。\x02\x03",

            "#1522F是『她』又是『武术家』的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B70")

    label("loc_1B07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(    #29
        0x106,
        (
            "#055F#6P喂喂……\x01",
            "好像有种不好的预感啊。\x02\x03",

            "是『她』又是『武术家』的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B70")

    Jump("loc_1BD4")

    label("loc_1B73")


    ChrTalk(    #30
        0x109,
        (
            "#1068F#6P喂喂……\x01",
            "这上面还有杀手锏啊！\x02\x03",

            "#1063F是『她』\x01",
            "又是『武术家』的话……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C4B")

    ChrTalk(    #31
        0x102,
        (
            "#1505F#6P……很有可能\x01",
            "是那个人吧。\x02\x03",

            "#1503F我听说\x01",
            "她已经回共和国去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2C")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(    #32
        0x102,
        (
            "#1505F#6P……很有可能\x01",
            "是那个人吧。\x02\x03",

            "#1503F我听说\x01",
            "她已经回共和国去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2C")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D2C")

    ChrTalk(    #33
        0x107,
        (
            "#065F#6P啊……\x01",
            "难、难、难不成……\x02\x03",

            "但、但是她应该\x01",
            "已经回共和国去了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(    #34
        0x10C,
        (
            "#115F#6P是吗……\x01",
            "我倒是听说过传闻。\x02\x03",

            "#112F据说被卡尔瓦德刚刚设立的\x01",
            "情报机关挖墙角了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE2")

    ChrTalk(    #35
        0x104,
        "#1541F#6P呼，原来如此，是她啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E21")

    ChrTalk(    #36
        0x105,
        "#1382F#6P原来如此……是那个人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E58")

    label("loc_1E21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E58")

    ChrTalk(    #37
        0x10E,
        "#178F#6P原来如此……是她啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB8")

    ChrTalk(    #38
        0x108,
        (
            "#075F#6P十有八九是没错的吧。\x02\x03",

            "#072F哎呀哎呀，\x01",
            "这下可不得了了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB8")


    ChrTalk(    #39
        0x10A,
        (
            "#819F#5P啊、啊哈哈……\x02\x03",

            "真希望是\x01",
            "预料错了啊……\x02",
        )
    )

    Jump("loc_1F06")

    label("loc_1F06")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F44")

    ChrTalk(    #40
        0x10F,
        "#1802F#6P（……到底是什么人？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F7B")

    label("loc_1F44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F7B")

    ChrTalk(    #41
        0x10B,
        "#216F#6P（什、什么人啊！？）\x02",
    )

    CloseMessageWindow()

    label("loc_1F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB6")

    ChrTalk(    #42
        0x110,
        "#1305F#6P（唔……真有趣呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FED")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FED")

    ChrTalk(    #43
        0x10D,
        "#277F#6P（唔……真有趣啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_1FED")

    OP_A2(0x2B12)
    OP_28(0x38, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_1221 end

    def Function_7_1FFE(): pass

    label("Function_7_1FFE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201F")
    Sleep(100)
    Jump("loc_209A")

    label("loc_201F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2034")
    Sleep(200)
    Jump("loc_209A")

    label("loc_2034")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2049")
    Sleep(300)
    Jump("loc_209A")

    label("loc_2049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_205E")
    Sleep(400)
    Jump("loc_209A")

    label("loc_205E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2073")
    Sleep(500)
    Jump("loc_209A")

    label("loc_2073")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2088")
    Sleep(600)
    Jump("loc_209A")

    label("loc_2088")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209A")
    Sleep(700)

    label("loc_209A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20BC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_209A")

    label("loc_20BC")

    Return()

    # Function_7_1FFE end

    def Function_8_20BD(): pass

    label("Function_8_20BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EA")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-142400, 0, 660, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    SetChrPos(0x109, -142810, 0, -130, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215E")
    SetChrPos(0xEF, -144570, 0, -400, 90)
    SetChrPos(0xF0, -146020, 0, -1350, 90)
    SetChrPos(0xF1, -145840, 0, 210, 90)
    Jump("loc_21E3")

    label("loc_215E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A2")
    SetChrPos(0xF0, -144570, 0, -400, 90)
    SetChrPos(0xEF, -146020, 0, -1350, 90)
    SetChrPos(0xF1, -145840, 0, 210, 90)
    Jump("loc_21E3")

    label("loc_21A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E3")
    SetChrPos(0xF1, -144570, 0, -400, 90)
    SetChrPos(0xEF, -146020, 0, -1350, 90)
    SetChrPos(0xF0, -145840, 0, 210, 90)

    label("loc_21E3")

    OP_0D()
    Sleep(300)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x0, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x07\x02#1S#40W人造之光照耀夜空。\x01",
            "请调查其底层吧。\x01",
            "如此汝即可获得光辉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #45
        "\x07\x00得到了\x1F\x31\x03\x07\x00。\x02",
    )

    Jump("loc_22AA")

    label("loc_22AA")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x331, 1)
    Sleep(500)
    OP_A2(0x2B13)
    OP_28(0x38, 0x1, 0x200)
    OP_74(0x0, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_2395")

    label("loc_22EA")

    TalkBegin(0xFF)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x0, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #46
        (
            "\x07\x02#1S#40W人造之光照耀夜空。\x01",
            "请调查其底层吧。\x01",
            "如此汝即可获得光辉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    FadeToBright(300, 0)
    OP_74(0x0, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    TalkEnd(0xFF)

    label("loc_2395")

    Return()

    # Function_8_20BD end

    SaveToFile()

Try(main)
