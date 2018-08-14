from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'P0312   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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


    DeclActor(
        TriggerX            = -2980,
        TriggerZ            = 0,
        TriggerY            = 66830,
        TriggerRange        = 800,
        ActorX              = -2980,
        ActorZ              = 1000,
        ActorY              = 66830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5110,
        TriggerZ            = 0,
        TriggerY            = 65500,
        TriggerRange        = 400,
        ActorX              = -5410,
        ActorZ              = 1500,
        ActorY              = 65800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61880,
        TriggerZ            = 0,
        TriggerY            = 6590,
        TriggerRange        = 1000,
        ActorX              = 62860,
        ActorZ              = 1000,
        ActorY              = 6490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 63000,
        TriggerZ            = 0,
        TriggerY            = -42000,
        TriggerRange        = 1000,
        ActorX              = 63000,
        ActorZ              = 1000,
        ActorY              = -42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_16A",          # 01, 1
        "Function_2_1CC",          # 02, 2
        "Function_3_2F2",          # 03, 3
        "Function_4_390",          # 04, 4
        "Function_5_4E2",          # 05, 5
        "Function_6_8B7",          # 06, 6
        "Function_7_951",          # 07, 7
        "Function_8_CE1",          # 08, 8
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_14D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_14D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169")
    Event(0, 4)

    label("loc_169")

    Return()

    # Function_0_13A end

    def Function_1_16A(): pass

    label("Function_1_16A")

    OP_B1("P0312_2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()

    label("loc_187")

    OP_72(0x405, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    OP_64(0x1, 0x1)

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB")
    OP_6F(0x6, 0)
    Jump("loc_1B2")

    label("loc_1AB")

    OP_6F(0x6, 60)

    label("loc_1B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4")
    OP_6F(0x7, 0)
    Jump("loc_1CB")

    label("loc_1C4")

    OP_6F(0x7, 60)

    label("loc_1CB")

    Return()

    # Function_1_16A end

    def Function_2_1CC(): pass

    label("Function_2_1CC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_240")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    Jump("loc_225")

    label("loc_225")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2692)
    Jump("loc_2AE")

    label("loc_240")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFC\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_28F")

    label("loc_28F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2AE")

    Jump("loc_2E4")

    label("loc_2B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1CC end

    def Function_3_2F2(): pass

    label("Function_3_2F2")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(300)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02３００米拉\x07\x00。\x02",
    )

    Jump("loc_350")

    label("loc_350")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2693)
    Jump("loc_37E")

    label("loc_362")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_37E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2F2 end

    def Function_4_390(): pass

    label("Function_4_390")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -3030, 0, 59570, 0)
    SetChrPos(0x10F, -2610, 0, 58260, 0)
    SetChrPos(0x107, -4440, 0, 57860, 0)
    OP_6D(-2250, 0, 59900, 0)
    OP_67(0, 6010, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x10F,
        "#1444F这里是……工房？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        (
            "#063F#6P嗯，是的。\x02\x03",

            "这里是维修班的成员\x01",
            "进行工作的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1065F#5P一个人都没有。\x02\x03",

            "#1067F真是……\x01",
            "到底去了哪里呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2614)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_4_390 end

    def Function_5_4E2(): pass

    label("Function_5_4E2")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -3100, 0, 65680, 0)
    SetChrPos(0x10F, -2420, 0, 64459, 0)
    SetChrPos(0x107, -3940, 0, 64099, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(-1970, 0, 66010, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1079F#5P这里……\x01",
            "应该是机关室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        (
            "#060F啊，是的。\x02\x03",

            "这里面收纳着\x01",
            "埃尔赛尤的主引擎——\x01",
            "八台新型引擎『ＸＧ－０２』……\x02\x03",

            "#560F对了对了，\x01",
            "让我来看看情况吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrPos(0x109, -3700, 0, 63900, 0)
    SetChrPos(0x10F, -2650, 0, 63440, 0)
    SetChrPos(0x107, -3110, 0, 65770, 180)
    OP_6D(-1930, 0, 65600, 0)
    OP_67(0, 5570, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(263, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x107,
        (
            "#561F#5P……不行……\x01",
            "一动也不动。\x02\x03",

            "而且找不到\x01",
            "无法启动的原因……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1067F#6P唔……原来如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1448F#4P……毕竟这里是\x01",
            "常识以外的法则在起作用的地方。\x02\x03",

            "机械之类的东西无法运作\x01",
            "也不奇怪吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#562F#5P呜呜……真没面子。\x02\x03",

            "#062F啊，不过不过，\x01",
            "预备导力的缆线\x01",
            "可以正常使用了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #14
        0x107,
        (
            "#560F#5P那边的终端\x01",
            "应该可以启动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1840F#6P是吗，真是帮大忙了。\x02\x03",

            "#1078F好，赶快调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2615)
    OP_65(0x1, 0x1)
    OP_28(0x29, 0x1, 0x400)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_5_4E2 end

    def Function_6_8B7(): pass

    label("Function_6_8B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -4480, 0, 65340, 0)
    SetChrPos(0x1, -5500, 0, 65180, 0)
    SetChrPos(0x2, -4710, 0, 64260, 0)
    SetChrPos(0x3, -5830, 0, 64099, 0)
    OP_6D(-4250, 0, 66180, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_8B7 end

    def Function_7_951(): pass

    label("Function_7_951")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x0, -4480, 0, 65340, 0)
    SetChrPos(0x1, -5500, 0, 65180, 0)
    SetChrPos(0x2, -4710, 0, 64260, 0)
    SetChrPos(0x3, -5830, 0, 64099, 0)
    OP_6D(-4250, 0, 66180, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("卡佩尔")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #16
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.8.0\x01",
            "MODE:Security Control\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1S进行紧急状态下的警卫系统的解除。\x01",
            "请选择想要解除的区域。\x02",
        )
    )

    Jump("loc_AC7")

    label("loc_AC7")

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD5")

    Menu(
        1,
        100,
        80,
        1,
        (
            "舰桥\x01",            # 0
            "作战会议室\x01",      # 1
            "医务室\x01",          # 2
            "中止操作\x01",        # 3
        )
    )

    Jump("loc_B2C")

    label("loc_B2C")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B4D"),
        (1, "loc_B98"),
        (2, "loc_BE3"),
        (SWITCH_DEFAULT, "loc_CB7"),
    )


    label("loc_B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 6)), scpexpr(EXPR_END)), "loc_B79")

    AnonymousTalk(    #17
        "\x07\x02#1S已经被解除了。\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B95")

    label("loc_B79")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_B95")

    Jump("loc_CD2")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 7)), scpexpr(EXPR_END)), "loc_BC4")

    AnonymousTalk(    #18
        "\x07\x02#1S已经被解除了。\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE0")

    label("loc_BC4")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_BE0")

    Jump("loc_CD2")

    label("loc_BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 0)), scpexpr(EXPR_END)), "loc_C0F")

    AnonymousTalk(    #19
        "\x07\x02#1S已经被解除了。\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB4")

    label("loc_C0F")

    OP_5F(0x1)
    OP_56(0x0)
    OP_A2(0x2618)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-1630, 0, -50570, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0x9C, 0x0, 0x64)
    OP_0D()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF)
    OP_73(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1003, 0x0)
    ExitThread()
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)

    label("loc_CB4")

    Jump("loc_CD2")

    label("loc_CB7")

    FadeToBright(300, 0)
    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CD2")

    label("loc_CD2")

    Jump("loc_ADB")

    label("loc_CD5")

    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_951 end

    def Function_8_CE1(): pass

    label("Function_8_CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF2")
    Call(0, 5)
    Return()

    label("loc_CF2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        (
            "\x07\x05　　 机关室\x01",
            "※无关人员禁止入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_CE1 end

    SaveToFile()

Try(main)
