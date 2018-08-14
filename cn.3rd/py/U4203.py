from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U4203   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4203.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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


    DeclEvent(
        X                   = -5190,
        Y                   = -1000,
        Z                   = 30500,
        Range               = 4870,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x7F62,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -4830,
        Y                   = -1000,
        Z                   = 39930,
        Range               = 5050,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xA758,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -4730,
        Y                   = -1000,
        Z                   = 44380,
        Range               = 5040,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xB324,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -12200,
        Y                   = -1000,
        Z                   = -12000,
        Range               = 11280,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xFFFFDA26,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = 7050,
        TriggerZ            = 0,
        TriggerY            = 11870,
        TriggerRange        = 1000,
        ActorX              = 8000,
        ActorZ              = 3000,
        ActorY              = 12000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14E",          # 00, 0
        "Function_1_178",          # 01, 1
        "Function_2_1E9",          # 02, 2
        "Function_3_2F6",          # 03, 3
        "Function_4_C87",          # 04, 4
        "Function_5_EAC",          # 05, 5
        "Function_6_F20",          # 06, 6
        "Function_7_10E9",         # 07, 7
        "Function_8_119F",         # 08, 8
        "Function_9_124A",         # 09, 9
        "Function_10_1250",        # 0A, 10
    )


    def Function_0_14E(): pass

    label("Function_0_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_164")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_177")

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_177")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_177")

    Return()

    # Function_0_14E end

    def Function_1_178(): pass

    label("Function_1_178")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    OP_22(0x1CC, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_1A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_END)), "loc_1BF")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 450)

    label("loc_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_1D2")
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()

    label("loc_1D2")

    OP_82(0x80, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1E5")
    OP_82(0x81, 0x0)
    Jump("loc_1E8")

    label("loc_1E5")

    OP_82(0x82, 0x0)

    label("loc_1E8")

    Return()

    # Function_1_178 end

    def Function_2_1E9(): pass

    label("Function_2_1E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 7700, 16000, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(0, 0)
    OP_6E(346, 0)

    def lambda_24C():
        OP_6D(0, 7500, 35300, 5500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_24C)

    def lambda_264():
        OP_67(0, 3640, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_264)

    def lambda_27C():
        OP_6B(2440, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_27C)

    def lambda_28C():
        OP_6E(325, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_28C)
    FadeToBright(2000, 0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(1000)

    def lambda_2B4():
        OP_6B(2200, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2B4)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1500)
    OP_20(0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x1CC)
    OP_21()
    OP_A2(0x250A)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1E9 end

    def Function_3_2F6(): pass

    label("Function_3_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 5)), scpexpr(EXPR_END)), "loc_301")
    Return()

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A")
    Return()

    label("loc_30A")

    EventBegin(0x0)
    OP_20(0x7D0)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_37B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_3A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3E2")

    label("loc_3CB")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3E2")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_40F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_476")

    label("loc_45F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_476")

    Sleep(1000)
    Fade(1000)
    OP_6D(0, 4300, 25980, 0)
    OP_67(0, 2470, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(0, 0)
    OP_6E(375, 0)
    SetChrPos(0x109, -470, 0, 27000, 0)
    SetChrPos(0x10F, 1000, 0, 26800, 0)
    SetChrPos(0xF0, -1080, 0, 24890, 0)
    SetChrPos(0xF1, 1480, 0, 24640, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)

    def lambda_52F():
        OP_6D(0, 4650, 43280, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_52F)

    def lambda_547():
        OP_67(0, 1000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_547)

    def lambda_55F():
        OP_6B(1800, 14000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_55F)

    def lambda_56F():
        OP_6E(580, 14000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_56F)
    OP_22(0x85, 0x1, 0x64)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x23)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)
    OP_23(0x85)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0xA, 0xA, 0x1388, 0x12C)
    Sleep(1000)
    WaitChrThread(0x109, 0x2)
    OP_1D(0xE6)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -320, 0, 40870, 0)
    SetChrPos(0x10F, 1220, 0, 40770, 0)
    SetChrPos(0xF0, -480, 0, 38690, 0)
    SetChrPos(0xF1, 1110, 0, 38690, 0)
    OP_6D(-190, 1750, 39470, 0)
    OP_67(0, 4430, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(309, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_693")

    ChrTalk(    #0
        0x107,
        "#065F#6P哇、哇啊……\x02",
    )

    CloseMessageWindow()

    label("loc_693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BC")

    ChrTalk(    #1
        0x10B,
        "#212F#6P呜……\x02",
    )

    CloseMessageWindow()

    label("loc_6BC")


    ChrTalk(    #2
        0x109,
        (
            "#1068F#6P哈哈，怎么说呢……\x01",
            "真是让人毛骨悚然啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        (
            "#1446F#5P因为是很古旧的城堡，\x01",
            "真是气氛十足啊。\x02\x03",

            "#1443F只是有点做作的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_825")

    ChrTalk(    #4
        0x10E,
        (
            "#175F#6P哼……\x01",
            "怎么可以这样！\x02\x03",

            "#178F凯文神父！\x01",
            "我们赶快进去吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7BE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7BE)
    Sleep(100)
    OP_8C(0x10F, 180, 400)

    ChrTalk(    #5
        0x109,
        (
            "#1065F#5P嗯，我知道了。\x02\x03",

            "#1063F那就……\x01",
            "做好准备往里面冲吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6F")

    label("loc_825")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_934")

    ChrTalk(    #6
        0x10D,
        (
            "#270F#6P凯文神父……\x01",
            "我们现在进去吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_879():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_879)
    Sleep(100)
    OP_8C(0x10F, 180, 400)

    ChrTalk(    #7
        0x109,
        (
            "#1065F#5P……不。\x01",
            "最好带上尤莉亚小姐\x01",
            "一起进去。\x02\x03",

            "#1063F她一直担心着\x01",
            "王城里面的人，\x01",
            "而且对城里也很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10D,
        "#277F#6P是啊……你说的没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_934")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2F")

    ChrTalk(    #9
        0x102,
        (
            "#1502F#6P……怎么办？\x01",
            "就这样继续往里走吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_97F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_97F)
    Sleep(100)
    OP_8C(0x10F, 180, 400)

    ChrTalk(    #10
        0x109,
        (
            "#1065F#5P……不。\x01",
            "最好带上尤莉亚小姐\x01",
            "一起进去。\x02\x03",

            "#1063F她一直担心着\x01",
            "王城里面的人，\x01",
            "而且对城里也很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#1500F#6P没错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B34")

    ChrTalk(    #12
        0x107,
        (
            "#063F#6P那个……\x01",
            "我们现在就要进去吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A75():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A75)
    Sleep(100)
    OP_8C(0x10F, 180, 400)

    ChrTalk(    #13
        0x109,
        (
            "#1065F#5P……不。\x01",
            "最好带上尤莉亚小姐\x01",
            "一起进去。\x02\x03",

            "#1063F她一直担心着\x01",
            "王城里面的人，\x01",
            "而且对城里也很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x107,
        (
            "#560F#6P是、是啊……\x01",
            "那就这样办吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34")


    ChrTalk(    #15
        0x10F,
        (
            "#1448F#5P我们先回据点一趟\x01",
            "把她带过来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2D, 0x1, 0x8)

    label("loc_B6F")

    Sleep(300)

    def lambda_B7A():
        OP_6B(3050, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B7A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2715)
    OP_28(0x2D, 0x1, 0x4)
    SetChrPos(0x0, 200, 0, 38220, 180)
    SetChrPos(0x1, 200, 0, 38220, 180)
    SetChrPos(0x2, 200, 0, 38220, 180)
    SetChrPos(0x3, 200, 0, 38220, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")
    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)

    label("loc_C32")

    OP_6D(200, 0, 38220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_2F6 end

    def Function_4_C87(): pass

    label("Function_4_C87")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C97")
    Return()

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA3")
    Return()

    label("loc_CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB2")
    Return()

    label("loc_CB2")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x109, 210, 0, 40660, 0)
    SetChrPos(0x10F, 230, 0, 38940, 0)
    SetChrPos(0xF0, -790, 0, 37610, 0)
    SetChrPos(0xF1, 1120, 0, 37800, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(1480, 0, 40650, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #16
        0x109,
        (
            "#1063F#5P（……进城之前\x01",
            "  还是先把尤莉亚小姐带来吧。）\x02\x03",

            "（她一直担心得不得了，\x01",
            "  而且对里面也很熟悉。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_28(0x2D, 0x1, 0x8)
    Fade(500)
    SetChrPos(0x0, 200, 0, 38220, 180)
    SetChrPos(0x1, 200, 0, 38220, 180)
    SetChrPos(0x2, 200, 0, 38220, 180)
    SetChrPos(0x3, 200, 0, 38220, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(200, 0, 38220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_4_C87 end

    def Function_5_EAC(): pass

    label("Function_5_EAC")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05打开『门』吗？\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_F09")

    label("loc_F09")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_5_EAC end

    def Function_6_F20(): pass

    label("Function_6_F20")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF6")
    OP_28(0xD, 0x4, 0x2)
    OP_82(0x81, 0x2)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_FF6")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #18
        (
            "\x07\x05#40W　　　汝须将王宫守护之刀，\x01",
            "　  与侍奉皇室之钢剑一同\x01",
            "　　   引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DD")
    Call(0, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA")
    Call(0, 7)

    label("loc_10DA")

    Jump("loc_10DD")

    label("loc_10DD")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_6_F20 end

    def Function_7_10E9(): pass

    label("Function_7_10E9")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0xC)
    Sleep(500)

    def lambda_1152():
        OP_6B(2830, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1152)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x0, 0, 0x0)
    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_10E9 end

    def Function_8_119F(): pass

    label("Function_8_119F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, 5590, 0, 12650, 90)
    SetChrPos(0x1, 5450, 0, 10750, 90)
    SetChrPos(0x2, 3540, 0, 12510, 90)
    SetChrPos(0x3, 3520, 0, 10430, 90)
    OP_6D(5630, 0, 11740, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_8_119F end

    def Function_9_124A(): pass

    label("Function_9_124A")

    SetMapFlags(0x2000000)
    Return()

    # Function_9_124A end

    def Function_10_1250(): pass

    label("Function_10_1250")

    ClearMapFlags(0x2000000)
    Return()

    # Function_10_1250 end

    SaveToFile()

Try(main)
