from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Kurt',                                 # 9
        'Jaeger Kurt',                          # 10
        'Jaeger Kurt',                          # 11
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
        "Function_4_12F5",         # 04, 4
        "Function_5_134A",         # 05, 5
        "Function_6_139F",         # 06, 6
        "Function_7_25B6",         # 07, 7
        "Function_8_2675",         # 08, 8
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
        "Male Voice",
        "#3PI'm glad you could make it, Anelace.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_453")

    label("loc_3EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_453")

    label("loc_414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_453")

    label("loc_43C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_453")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E7")

    label("loc_480")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E7")

    label("loc_4A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E7")

    label("loc_4D0")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4E7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_53C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_564")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_57B")

    label("loc_564")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_57B")

    Sleep(1000)

    def lambda_586():
        OP_6D(-145190, 0, 850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_586)

    def lambda_59E():
        OP_67(0, 5860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_59E)

    def lambda_5B6():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5B6)

    def lambda_5C6():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5C6)

    def lambda_5D6():
        OP_6E(250, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5D6)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #1
        0x10A,
        "#1317F#2PS-So it really is you...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-148200, 0, 1650, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)

    def lambda_659():
        OP_8F(0xFE, 0xFFFDABA2, 0x0, 0xFFFFFBDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_659)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")

    def lambda_687():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_687)
    Sleep(100)

    def lambda_6A7():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6A7)
    Sleep(100)

    def lambda_6C7():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_6C7)
    Jump("loc_7B4")

    label("loc_6DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")

    def lambda_6F3():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_6F3)
    Sleep(100)

    def lambda_713():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_713)
    Sleep(100)

    def lambda_733():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_733)
    Jump("loc_7B4")

    label("loc_74B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B4")

    def lambda_75F():
        OP_8F(0xFE, 0xFFFDABC0, 0x0, 0x276, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_75F)
    Sleep(100)

    def lambda_77F():
        OP_8F(0xFE, 0xFFFDA544, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_77F)
    Sleep(100)

    def lambda_79F():
        OP_8F(0xFE, 0xFFFDA60C, 0x0, 0x1FE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_79F)

    label("loc_7B4")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #2
        0x10,
        (
            "#843F#11PIt's good to see a number of familiar faces\x01",
            "among you.\x02\x03",

            "#845FBut what a cruel twist of fate that we should\x01",
            "have to meet again like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89F")

    ChrTalk(    #3
        0x103,
        "#1525F#6P*sigh* You're telling me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_89F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D5")

    ChrTalk(    #4
        0x106,
        "#051F#6PHeh. You're tellin' me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_909")

    ChrTalk(    #5
        0x101,
        "#1019F#6PYou're telling me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_976")

    label("loc_909")


    ChrTalk(    #6
        0x109,
        (
            "#1840F#6PY-You're telling me... Hard to make with the\x01",
            "happy reunion and the Goddess-thanking like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_976")


    ChrTalk(    #7
        0x10A,
        (
            "#1317F#6PU-Umm...\x02\x03",

            "#819FSo you plan on fighting us for real, too, then?\x02\x03",

            "There's no way we could, you know, talk you\x01",
            "out of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#844F#11PI'm afraid that doesn't appear to be an option.\x02\x03",

            "#843FSince I first became conscious of my existence\x01",
            "here, I've attempted to meditate on a number\x01",
            "of occasions...\x02\x03",

            "#842F...but it appears the 'me' before you lacks a\x01",
            "sense of self, as it were--and so I am unable to\x01",
            "go against the purpose for which I was created.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10A,
        (
            "#1316F#6P*sigh* Of COURSE you'd try to meditate right\x01",
            "away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1075F#6PYou really are a special guy, Kurt.\x02\x03",

            "#1840FWell, don't think we've got any choice but to\x01",
            "resign ourselves to the inevitable and get on\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#841F#11PI believe so. I look forward to seeing what you\x01",
            "can do.\x02",
        )
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

    def lambda_C91():

        label("loc_C91")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_C91")

    QueueWorkItem2(0x10, 3, lambda_C91)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_CE0():
        OP_6D(-150200, 0, 1020, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_CE0)

    def lambda_CF8():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_CF8)

    def lambda_D10():
        OP_6B(2820, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_D10)

    def lambda_D20():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D20)

    def lambda_D30():
        OP_6E(335, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_D30)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -152830, 0, 5260, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, -152330, 0, -5530, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE0")

    def lambda_DC2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_DC2)
    Sleep(50)

    def lambda_DD5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_DD5)
    Jump("loc_E41")

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E12")

    def lambda_DF4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_DF4)
    Sleep(50)

    def lambda_E07():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_E07)
    Jump("loc_E41")

    label("loc_E12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E41")

    def lambda_E26():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_E26)
    Sleep(50)

    def lambda_E39():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_E39)

    label("loc_E41")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -152830, -3000, 5260, 180)
    SetChrPos(0x12, -152330, -3000, -5530, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_E78():

        label("loc_E78")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_E78")

    QueueWorkItem2(0x109, 3, lambda_E78)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F06")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6D")

    label("loc_F06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6D")

    label("loc_F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F56")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F6D")

    label("loc_F56")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F6D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9A")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1001")

    label("loc_F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1001")

    label("loc_FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1001")

    label("loc_FEA")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1001")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1095")

    label("loc_102E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1095")

    label("loc_1056")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1095")

    label("loc_107E")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1095")

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
            "#812F#6PUgh... Fighting three of him from his favorite\x01",
            "attack range isn't going to be easy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        "#1069F#6PThis is gonna be a tough one, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#843F#11PMy formation is flexible yet resilient, \x01",
            "much like nature itself!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #15
        0x10,
        "#846F#11P#4SNow, let our battle begin!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1229():
        OP_6D(-151200, 0, 800, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1229)

    def lambda_1241():
        OP_67(0, 6000, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1241)

    def lambda_1259():
        OP_6B(2350, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1259)

    def lambda_1269():
        OP_6E(290, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1269)
    SetChrChipByIndex(0x10, 7)

    def lambda_127E():
        OP_8F(0xFE, 0xFFFDAFDA, 0x0, 0xFFFFFF6A, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_127E)
    SetChrChipByIndex(0x11, 11)

    def lambda_129E():
        OP_8F(0xFE, 0xFFFDA7E2, 0x0, 0xDC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_129E)
    SetChrChipByIndex(0x12, 11)

    def lambda_12BE():
        OP_8F(0xFE, 0xFFFDA8DC, 0x0, 0xFFFFFAC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_12BE)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1BA end

    def Function_4_12F5(): pass

    label("Function_4_12F5")

    PlayEffect(0x1, 0x4, 0xFF, -152830, 0, 5260, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_12F5 end

    def Function_5_134A(): pass

    label("Function_5_134A")

    PlayEffect(0x1, 0x5, 0xFF, -152330, 0, -5530, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_134A end

    def Function_6_139F(): pass

    label("Function_6_139F")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BB")
    SetChrPos(0xEF, -149200, 0, 440, 90)
    SetChrPos(0xF0, -150790, 0, -1320, 90)
    SetChrPos(0xF1, -150800, 0, 370, 90)
    Jump("loc_1540")

    label("loc_14BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    SetChrPos(0xF0, -149200, 0, 440, 90)
    SetChrPos(0xEF, -150790, 0, -1320, 90)
    SetChrPos(0xF1, -150800, 0, 370, 90)
    Jump("loc_1540")

    label("loc_14FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1540")
    SetChrPos(0xF1, -149200, 0, 440, 90)
    SetChrPos(0xEF, -150790, 0, -1320, 90)
    SetChrPos(0xF0, -150800, 0, 370, 90)

    label("loc_1540")

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
            "#843F#11PHaha... I see I still have much room for\x01",
            "improvement...\x02\x03",

            "#845FI can only hope the knowledge I have gained\x01",
            "from this battle will find its way to my real self\x01",
            "as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        (
            "#1314F#6PHaha... I don't think I've ever met anyone as\x01",
            "serious about their training as you, Kurt.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175C")

    ChrTalk(    #18
        0x101,
        (
            "#1007F#6PI-It's no wonder you're way stronger than\x01",
            "when we last fought if you take bettering\x01",
            "yourself THAT seriously...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(    #19
        0x106,
        "#552F#6PAddicted to training much, man?\x02",
    )

    CloseMessageWindow()

    label("loc_1797")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FB")

    ChrTalk(    #20
        0x103,
        (
            "#1534F#6PHonestly...your devotion to honing your craft\x01",
            "never ceases to amaze me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FB")


    ChrTalk(    #21
        0x10,
        (
            "#843F#11PWith promising young bracers like you around,\x01",
            "I can't very well afford to rest on my laurels.\x02\x03",

            "#840FStill, with the skills you demonstrated there,\x01",
            "perhaps you have a chance at defeating her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1973")

    label("loc_190C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1934")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1973")

    label("loc_1934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1973")

    label("loc_195C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1973")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A07")

    label("loc_19A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A07")

    label("loc_19C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A07")

    label("loc_19F0")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A07")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A34")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A9B")

    label("loc_1A34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A9B")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A84")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A9B")

    label("loc_1A84")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A9B")

    Sleep(1000)

    ChrTalk(    #22
        0x10A,
        "#1317F#6P...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1069F#6PW-Wait a sec! I thought you were the last person\x01",
            "we had to fight here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#843F#11PHaha... I'm afraid not. Another foe awaits you on\x01",
            "this building's highest floor.\x02\x03",

            "#841FBut don't even think of taking her lightly. She is\x01",
            "formidable in every sense of the word.\x02\x03",

            "Her martial arts skills given her age are nothing\x01",
            "short of exceptional.\x02\x03",

            "So if you try challenging her with any less than\x01",
            "your best, you won't last.\x02",
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

    def lambda_1CBB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1CBB)
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
        "#1317F#5PUmm...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FA9")

    ChrTalk(    #26
        0x109,
        (
            "#1068F#6POh, lucky us. I thought we were home free from\x01",
            "here, and now there's someone ELSE?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E50")

    ChrTalk(    #27
        0x101,
        (
            "#1007F#6PI've got a really bad feeling as to who it could\x01",
            "be, too.\x02\x03",

            "#1019FI mean, I don't know that many martial artists\x01",
            "out there who could wipe the floor with us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA6")

    label("loc_1E50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EF9")

    ChrTalk(    #28
        0x103,
        (
            "#1525F#6P*sigh* I've got a really bad feeling on who she\x01",
            "is, too.\x02\x03",

            "#1522FI can't say I know a whole lot of martial artists\x01",
            "who are THAT dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA6")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FA6")

    ChrTalk(    #29
        0x106,
        (
            "#055F#6PI've got a real bad feeling who it could be,\x01",
            "too...\x02\x03",

            "Not a whole lotta martial artists who could\x01",
            "kick our asses into next week the way she\x01",
            "could.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA6")

    Jump("loc_207D")

    label("loc_1FA9")


    ChrTalk(    #30
        0x109,
        (
            "#1068F#6POh, lucky us. I thought we were home free\x01",
            "from here, and now there's someone ELSE?!\x02\x03",

            "#1063FAnd if it's the first person who comes to mind\x01",
            "when I think of martial artists, we're in biiiiiig\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_211C")

    ChrTalk(    #31
        0x102,
        (
            "#1505F#6PI think it's safe to say he was referring to her,\x01",
            "yeah.\x02\x03",

            "#1503FI'd heard she had returned home to Calvard,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2224")

    label("loc_211C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21BB")

    ChrTalk(    #32
        0x102,
        (
            "#1505F#6PI think it's safe to say he was referring to her,\x01",
            "yeah.\x02\x03",

            "#1503FI'd heard she had returned home to Calvard,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2224")

    label("loc_21BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(    #33
        0x107,
        (
            "#065F#6PC-Could it be...you know...?\x02\x03",

            "I thought she'd gone home to Calvard, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D4")

    ChrTalk(    #34
        0x10C,
        (
            "#115F#6PI think I may well know who he means as well.\x02\x03",

            "#112FShe was supposedly recruited to join a recently\x01",
            "established intelligence agency in Calvard, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2314")

    ChrTalk(    #35
        0x104,
        "#1541F#6PWell, aren't we in for some fun?\x02",
    )

    CloseMessageWindow()
    Jump("loc_23B4")

    label("loc_2314")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2366")

    ChrTalk(    #36
        0x105,
        "#1382F#6PI think I know who we're talking about now, too...\x02",
    )

    CloseMessageWindow()
    Jump("loc_23B4")

    label("loc_2366")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B4")

    ChrTalk(    #37
        0x10E,
        "#178F#6PI think I know who we're talking about now, too...\x02",
    )

    CloseMessageWindow()

    label("loc_23B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2442")

    ChrTalk(    #38
        0x108,
        (
            "#075F#6PNo reason for me to point out the obvious, now,\x01",
            "is there?\x02\x03",

            "#072F...I think we all know this isn't going to be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2442")


    ChrTalk(    #39
        0x10A,
        (
            "#819F#5PA-Ahaha...\x02\x03",

            "I REALLY hope we're wrong this time...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C4")

    ChrTalk(    #40
        0x10F,
        "#1802F#6P(Who could they be talking about?)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2525")

    label("loc_24C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2525")

    ChrTalk(    #41
        0x10B,
        (
            "#216F#6P(I-I dunno who they're talking about,\x01",
            "but she sounds really scary...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2525")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(    #42
        0x110,
        "#1305F#6P(Now I'm REALLY curious...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A5")

    label("loc_2560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A5")

    ChrTalk(    #43
        0x10D,
        "#277F#6P(Hmm... I'm curious who they could mean.)\x02",
    )

    CloseMessageWindow()

    label("loc_25A5")

    OP_A2(0x2B12)
    OP_28(0x38, 0x1, 0x100)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_6_139F end

    def Function_7_25B6(): pass

    label("Function_7_25B6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D7")
    Sleep(100)
    Jump("loc_2652")

    label("loc_25D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25EC")
    Sleep(200)
    Jump("loc_2652")

    label("loc_25EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2601")
    Sleep(300)
    Jump("loc_2652")

    label("loc_2601")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2616")
    Sleep(400)
    Jump("loc_2652")

    label("loc_2616")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262B")
    Sleep(500)
    Jump("loc_2652")

    label("loc_262B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2640")
    Sleep(600)
    Jump("loc_2652")

    label("loc_2640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2652")
    Sleep(700)

    label("loc_2652")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2674")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_2652")

    label("loc_2674")

    Return()

    # Function_7_25B6 end

    def Function_8_2675(): pass

    label("Function_8_2675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D4")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-142400, 0, 660, 0)
    OP_67(0, 6450, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    SetChrPos(0x109, -142810, 0, -130, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2716")
    SetChrPos(0xEF, -144570, 0, -400, 90)
    SetChrPos(0xF0, -146020, 0, -1350, 90)
    SetChrPos(0xF1, -145840, 0, 210, 90)
    Jump("loc_279B")

    label("loc_2716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275A")
    SetChrPos(0xF0, -144570, 0, -400, 90)
    SetChrPos(0xEF, -146020, 0, -1350, 90)
    SetChrPos(0xF1, -145840, 0, 210, 90)
    Jump("loc_279B")

    label("loc_275A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_279B")
    SetChrPos(0xF1, -144570, 0, -400, 90)
    SetChrPos(0xEF, -146020, 0, -1350, 90)
    SetChrPos(0xF0, -145840, 0, 210, 90)

    label("loc_279B")

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
            "\x07\x02#1S#40WInvestigate what boldly shines\x01",
            "its artificial lights to embolden\x01",
            "the night sky,\x01",
            "then you shall obtain radiance.\x02",
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
        "\x07\x05Received \x1F\x31\x03\x07\x05.\x02",
    )

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
    Jump("loc_29B6")

    label("loc_28D4")

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
            "\x07\x02#1S#40WInvestigate what boldly shines\x01",
            "its artificial lights to embolden\x01",
            "the night sky,\x01",
            "then you shall obtain radiance.\x02",
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

    label("loc_29B6")

    Return()

    # Function_8_2675 end

    SaveToFile()

Try(main)
