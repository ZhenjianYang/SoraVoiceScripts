from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
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
        '',                                     # 8
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
        Unknown_30              = 35,
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_489",          # 01, 1
        "Function_2_FF8",          # 02, 2
        "Function_3_10A9",         # 03, 3
        "Function_4_1618",         # 04, 4
        "Function_5_2FCF",         # 05, 5
        "Function_6_3309",         # 06, 6
        "Function_7_3E26",         # 07, 7
        "Function_8_3FBE",         # 08, 8
        "Function_9_442A",         # 09, 9
        "Function_10_4FE8",        # 0A, 10
        "Function_11_5808",        # 0B, 11
        "Function_12_5E2C",        # 0C, 12
        "Function_13_6A4D",        # 0D, 13
        "Function_14_700F",        # 0E, 14
        "Function_15_7346",        # 0F, 15
        "Function_16_7439",        # 10, 16
        "Function_17_777D",        # 11, 17
        "Function_18_7B5A",        # 12, 18
        "Function_19_7F7F",        # 13, 19
        "Function_20_8906",        # 14, 20
        "Function_21_9077",        # 15, 21
        "Function_22_9201",        # 16, 22
        "Function_23_98EE",        # 17, 23
        "Function_24_9DCD",        # 18, 24
        "Function_25_A681",        # 19, 25
        "Function_26_B732",        # 1A, 26
        "Function_27_B740",        # 1B, 27
        "Function_28_B76D",        # 1C, 28
        "Function_29_B79A",        # 1D, 29
        "Function_30_B7D7",        # 1E, 30
        "Function_31_B814",        # 1F, 31
        "Function_32_B829",        # 20, 32
        "Function_33_B83E",        # 21, 33
        "Function_34_B853",        # 22, 34
        "Function_35_B868",        # 23, 35
        "Function_36_B8AB",        # 24, 36
        "Function_37_B8DF",        # 25, 37
        "Function_38_B913",        # 26, 38
        "Function_39_B947",        # 27, 39
        "Function_40_B97B",        # 28, 40
        "Function_41_B9D4",        # 29, 41
        "Function_42_B9DC",        # 2A, 42
        "Function_43_B9E4",        # 2B, 43
        "Function_44_BA0D",        # 2C, 44
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    TurnDirection(0x1, 0xE, 0)
    TurnDirection(0x2, 0xE, 0)
    TurnDirection(0x3, 0xE, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_170")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_12F")

    ChrTalk(    #0
        0xE,
        (
            "不过，怀疑昆茨\x01",
            "看来是太草率了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xE,
        (
            "关于这件事有机会\x01",
            "一定要向他道歉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D")

    label("loc_12F")

    OP_A2(0x8)

    ChrTalk(    #2
        0xE,
        (
            "哎呀，各位。\x01",
            "今天非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        "让我再次向你们道谢。\x02",
    )

    CloseMessageWindow()

    label("loc_16D")

    Jump("loc_488")

    label("loc_170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1C9")

    ChrTalk(    #4
        0xE,
        (
            "啊，游击士。\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "以后再有什么事情的话\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_488")

    label("loc_1C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_38F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1DE")
    Jump("loc_1F0")

    label("loc_1DE")


    ChrTalk(    #6
        0xE,
        "咦？不们……\x02",
    )

    CloseMessageWindow()

    label("loc_1F0")


    ChrTalk(    #7
        0xE,
        (
            "你们\x01",
            "能帮忙调查吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")

    ChrTalk(    #8
        0x101,
        "#1006F嗯，没问题。\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #9
        0xE,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xE,
        "谢谢，我会记着这份人情的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xE,
        (
            "来，进来吧。\x01",
            "马上来介绍给你们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 4)
    OP_A2(0xA)
    Jump("loc_38C")

    label("loc_312")


    ChrTalk(    #12
        0x101,
        (
            "#1007F对、对不起。\x02\x03",

            "还是不行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #13
        0xE,
        "那、那样啊…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "没办法，我就先放弃了，\x01",
            "等其它的游击士们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_8C(0xE, 90, 0)

    label("loc_38C")

    Jump("loc_488")

    label("loc_38F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_402")

    ChrTalk(    #15
        0xE,
        (
            "现在在进行重要的会议，\x01",
            "很遗憾我不能让你们进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xE,
        (
            "十分抱歉，\x01",
            "如果有事的话请以后再来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_481")

    label("loc_402")

    OP_A2(0x8)

    ChrTalk(    #17
        0xE,
        "这里是诺曼的选举事务所。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        (
            "现在在进行重要的会议，\x01",
            "很遗憾我不能让你们进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xE,
        (
            "十分抱歉，如果有事的话\x01",
            "请以后再来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481")

    OP_8C(0xE, 90, 0)

    label("loc_488")

    Return()

    # Function_0_AA end

    def Function_1_489(): pass

    label("Function_1_489")

    OP_A3(0xA)
    OP_4A(0xE, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC3")
    TalkBegin(0xE)
    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DA"),
        (1, "loc_5A9"),
        (2, "loc_77C"),
        (3, "loc_80C"),
        (4, "loc_8E1"),
        (5, "loc_C7B"),
        (6, "loc_DE8"),
        (7, "loc_F0B"),
        (SWITCH_DEFAULT, "loc_FBA"),
    )


    label("loc_4DA")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_53C")

    ChrTalk(    #20
        0xFE,
        (
            "那时昆茨先生的\x01",
            "表情非常吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "自己的罪行被目击了，\x01",
            "吃惊也很正常。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A6")

    label("loc_53C")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #22
        0xFE,
        (
            "一看到我们\x01",
            "昆茨先生就露出了吃惊的表情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "一定是因为自己的罪行被目击了\x01",
            "就惊惶失措了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A6")

    Jump("loc_FBD")

    label("loc_5A9")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_655")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_60C")

    ChrTalk(    #24
        0xFE,
        (
            "我没听到过\x01",
            "那么大的声响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我能断言我在\x01",
            "那里时没听到过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_652")

    label("loc_60C")


    ChrTalk(    #26
        0xFE,
        (
            "房间里确实\x01",
            "一直都很安静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "如果有口角的话\x01",
            "我一定会注意到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_652")

    Jump("loc_779")

    label("loc_655")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #28
        0xFE,
        (
            "确、确实如\x01",
            "昆茨先生所说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "我在门口守着，\x01",
            "不过房间里一直都很安静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "如果有口角的话\x01",
            "我一定会注意到的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #31
        0x101,
        (
            "#1015F可是说到巨大的响声，\x01",
            "有人可以作证呢。\x02\x03",

            "#1002F说是在阳台下听到了\x01",
            "物体碰撞的声音哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #32
        0xFE,
        "不，我没听见。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "我能断言我在\x01",
            "那里时没听到过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_779")

    Jump("loc_FBD")

    label("loc_77C")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7CE")

    ChrTalk(    #34
        0xFE,
        (
            "昆茨先生和平时\x01",
            "没什么两样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "也看不出\x01",
            "他在生气……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_809")

    label("loc_7CE")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #36
        0xFE,
        "昆茨先生生气了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "不过我可没\x01",
            "看出来……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_809")

    Jump("loc_FBD")

    label("loc_80C")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_868")

    ChrTalk(    #38
        0xFE,
        (
            "我也是人啊，\x01",
            "也会有脸色不好的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "但是那跟案子\x01",
            "没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DE")

    label("loc_868")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #40
        0xFE,
        "说我脸色不好？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "那、那也是没办法的吧，\x01",
            "因为遇上了那样的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "那么，这和案子\x01",
            "又有什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DE")

    Jump("loc_FBD")

    label("loc_8E1")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_96E")

    ChrTalk(    #43
        0xFE,
        (
            "我确实上了２楼，\x01",
            "不过只是因为有东西忘在那里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "反正是无关紧要的事，\x01",
            "我也没特意告诉你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BE")

    label("loc_96E")


    ChrTalk(    #45
        0xFE,
        (
            "午饭之后，我和诺曼先生\x01",
            "去演说的地方预练了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "虽然我有事\x01",
            "迟到了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BE")

    Jump("loc_C78")

    label("loc_9C1")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #47
        0xFE,
        (
            "午饭之后，我和诺曼先生\x01",
            "去演说的地方预练了一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "虽然我有事\x01",
            "迟到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "后来就和我前面说过的一样。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_C78")
    OP_28(0x69, 0x1, 0x20)

    ChrTalk(    #50
        0x101,
        (
            "#1002F……不过，海利欧先生。\x02\x03",

            "你在此之前上了２楼吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #51
        0xFE,
        "啊……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1002F隐瞒也没用。\x01",
            "有人目击到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #53
        0xFE,
        "我、我没有隐瞒！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "我、我只是想起有东西忘在事务所，\x01",
            "所以就急忙回去了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1002F那时候事务所里有些什么人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "德尔斯在里面工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "我没看见其它人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1000F嗯，了解到这些就够了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "那、那个……\x01",
            "请别误解啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "我并无意要\x01",
            "隐瞒上２楼的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1010F不用担心。\x01",
            "我们也没确定谁是犯人。\x02\x03",

            "#1002F不过，希望你能明白\x01",
            "这么做会使自己变得不利。\x02\x03",

            "那么，今后也请尽量合作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78")

    Jump("loc_FBD")

    label("loc_C7B")

    OP_28(0x6A, 0x1, 0x400)

    ChrTalk(    #62
        0xFE,
        "我在外面听到过钟声。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "应该是在桥边遇见\x01",
            "诺曼先生的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "然后昆茨先生也来了，\x01",
            "我就把他带到了这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB4")
    OP_28(0x69, 0x1, 0x200)

    ChrTalk(    #65
        0x101,
        (
            "#1015F海利欧先生在外面\x01",
            "听到了钟声……\x02\x03",

            "就是说和那个响声无关了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        (
            "#042F根据证词，响声发生在\x01",
            "钟声刚结束之后……\x02\x03",

            "如果这话是真的，\x01",
            "那就是无关的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE5")

    label("loc_DB4")


    ChrTalk(    #67
        0x101,
        (
            "#1002F原来如此……\x01",
            "和诺曼先生的证词一致呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE5")

    Jump("loc_FBD")

    label("loc_DE8")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_E4C")

    ChrTalk(    #68
        0xFE,
        (
            "看来是在我出去的\x01",
            "时候有人做了收拾善后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "亚内斯特以往\x01",
            "就是这么做的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F08")

    label("loc_E4C")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #70
        0xFE,
        (
            "收拾善后？\x01",
            "我不知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "大概，在我外出期间\x01",
            "有人做了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1002F在你外出前回到事务所时，\x01",
            "餐具已经被收拾好了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "嗯，让我想想……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "我没仔细看，\x01",
            "所以也说不清楚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F08")

    Jump("loc_FBD")

    label("loc_F0B")

    OP_28(0x6A, 0x1, 0x400)
    Jc((scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_F67")

    ChrTalk(    #75
        0xFE,
        (
            "你问我贝尔夫在哪里\x01",
            "我也不知道啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "因为钟响的时候\x01",
            "我出去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB7")

    label("loc_F67")

    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #77
        0xFE,
        (
            "钟响的时候\x01",
            "贝尔夫在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "那个我不知道。\x01",
            "因为当时我出去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB7")

    Jump("loc_FBD")

    label("loc_FBA")

    Jump("loc_FBD")

    label("loc_FBD")

    TalkEnd(0xE)
    Jump("loc_FF3")

    label("loc_FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE9")
    EventBegin(0x2)
    Call(1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE6")
    EventEnd(0x3)

    label("loc_FE6")

    Jump("loc_FF3")

    label("loc_FE9")

    TalkBegin(0xE)
    Call(1, 0)
    TalkEnd(0xE)

    label("loc_FF3")

    OP_4B(0xE, 0)
    Return()

    # Function_1_489 end

    def Function_2_FF8(): pass

    label("Function_2_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1000")
    Return()

    label("loc_1000")

    OP_A3(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_106A")
    EventBegin(0x1)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    OP_4A(0xE, 0)
    Call(1, 0)
    OP_4B(0xE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1066")
    OP_8C(0xE, 90, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_1067")

    label("loc_1066")

    Return()

    label("loc_1067")

    Jump("loc_10A8")

    label("loc_106A")

    EventBegin(0x1)
    TurnDirection(0xE, 0x0, 0)
    TurnDirection(0x0, 0xE, 0)
    OP_4A(0xE, 255)
    Call(1, 0)
    OP_8C(0xE, 90, 0)
    OP_4B(0xE, 255)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_10A8")

    Return()

    # Function_2_FF8 end

    def Function_3_10A9(): pass

    label("Function_3_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10B1")
    Return()

    label("loc_10B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1617")
    EventBegin(0x0)
    OP_4A(0xE, 0)
    SetChrPos(0xE, -2340, 0, 9540, 180)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_28(0x6A, 0x1, 0x8000)
    OP_6D(1780, 0, 2230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 4450, 0, 2400, 270)
    SetChrPos(0xF7, 5150, -50, 1910, 270)
    SetChrPos(0x104, 5700, -550, 2370, 270)
    SetChrPos(0x105, 6350, -1050, 1780, 270)
    OP_43(0x101, 0x1, 0x1, 0x1F)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x1, 0x20)
    Sleep(300)
    OP_43(0x104, 0x1, 0x1, 0x21)
    Sleep(300)
    OP_43(0x105, 0x1, 0x1, 0x22)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #79
        0xE,
        "青年的声音",
        "啊！你、你们！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_11E0():

        label("loc_11E0")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_11E0")

    QueueWorkItem2(0x101, 1, lambda_11E0)
    Sleep(200)

    def lambda_11F6():

        label("loc_11F6")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_11F6")

    QueueWorkItem2(0xF7, 1, lambda_11F6)

    def lambda_1207():

        label("loc_1207")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1207")

    QueueWorkItem2(0x104, 1, lambda_1207)

    def lambda_1218():

        label("loc_1218")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_1218")

    QueueWorkItem2(0x105, 1, lambda_1218)
    OP_6D(-1610, 0, 6840, 2000)

    def lambda_123A():
        OP_6D(-170, 0, 2320, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_123A)
    OP_8E(0xE, 0xFFFFFCCC, 0x0, 0x8E8, 0xBB8, 0x0)
    WaitChrThread(0xE, 0x1)
    TurnDirection(0xE, 0x101, 400)
    WaitChrThread(0xE, 0x2)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)

    ChrTalk(    #80
        0xE,
        "呼～呼～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xE,
        "你、你们是游击士吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1002F是的……有什么问题吗？\x02\x03",

            "你好像很慌乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xE,
        (
            "我、我有事想请你们\x01",
            "马上调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xE,
        "能不能马上跟我来？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【不】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1537")

    ChrTalk(    #85
        0x101,
        (
            "#1015F抱歉啊，现在不行。\x02\x03",

            "我们正准备\x01",
            "出发去其它地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        "啊，是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13DB")

    ChrTalk(    #87
        0x106,
        "#050F你联络协会了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1401")

    label("loc_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(    #88
        0x103,
        "#022F你已经联络协会了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1401")


    ChrTalk(    #89
        0xE,
        "嗯，刚联络过。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xE,
        (
            "没办法，我就等\x01",
            "其它游击士来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1007F真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        "没关系，大家都很忙啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xE,
        "那我就先告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_148A():

        label("loc_148A")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_148A")

    QueueWorkItem2(0x0, 1, lambda_148A)

    def lambda_149B():

        label("loc_149B")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_149B")

    QueueWorkItem2(0x1, 1, lambda_149B)

    def lambda_14AC():

        label("loc_14AC")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_14AC")

    QueueWorkItem2(0x2, 1, lambda_14AC)

    def lambda_14BD():

        label("loc_14BD")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_14BD")

    QueueWorkItem2(0x3, 1, lambda_14BD)
    OP_8E(0xE, 0x5DC, 0x0, 0x82, 0x7D0, 0x0)
    OP_8E(0xE, 0x173E, 0x8CA, 0xA0, 0x7D0, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8E(0xE, 0x173E, 0x8CA, 0x7B2, 0x7D0, 0x0)
    Sleep(400)
    SetChrPos(0xE, 22470, 0, 76980, 90)
    OP_28(0x6A, 0x1, 0x4000)
    OP_4B(0xE, 255)
    EventEnd(0x0)
    Return()

    label("loc_1537")


    ChrTalk(    #94
        0x101,
        "#1006F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        "谢谢，我会记着这份人情的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1598")

    ChrTalk(    #96
        0x106,
        "#050F那么我们应该去哪里？\x02",
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_1598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_15BE")

    ChrTalk(    #97
        0x103,
        "#020F那么我们应该去哪里？\x02",
    )

    CloseMessageWindow()

    label("loc_15BE")


    ChrTalk(    #98
        0xE,
        (
            "去这座酒店最顶层的\x01",
            "诺曼先生选举事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xE,
        "我立刻带你们去。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 4)
    EventEnd(0x0)

    label("loc_1617")

    Return()

    # Function_3_10A9 end

    def Function_4_1618(): pass

    label("Function_4_1618")

    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x0, 1500, 0, 79940, 274)
    SetChrPos(0xB, -3200, 0, 81000, 90)
    SetChrPos(0x14, -2140, 0, 81000, 270)
    OP_6D(-2540, 0, 80960, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    EventBegin(0x0)
    OP_4A(0xB, 0)
    OP_4A(0x14, 0)
    OP_4A(0xE, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #100
        0x14,
        (
            "我～都～说～了，\x01",
            "不是我干的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x14,
        (
            "快点让我回去吧！\x01",
            "我也有事情要办啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xB,
        "#1P好了，冷静一点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        (
            "#1P你就忍耐到游击士来吧。\x01",
            "调查结束了马上就能回去。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_70(0x6, 0x1D)
    OP_73(0x6)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #104
        0xB,
        (
            "#1P看，刚说\x01",
            "他们就来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-1280, 0, 79170, 1500)
    OP_43(0xE, 0x1, 0x1, 0x24)
    OP_8C(0x14, 180, 400)
    Sleep(600)

    def lambda_17DF():
        OP_6D(-2420, 0, 79460, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_17DF)
    OP_43(0x101, 0x1, 0x1, 0x25)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_180E")
    OP_43(0x106, 0x1, 0x1, 0x26)
    Jump("loc_181C")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_181C")
    OP_43(0x103, 0x1, 0x1, 0x26)

    label("loc_181C")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x27)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0x28)
    Sleep(300)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x14, 0x2)
    TurnDirection(0xB, 0xE, 400)

    ChrTalk(    #105
        0xB,
        (
            "海利欧，\x01",
            "你挺快的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xE,
        (
            "嗯，运气不错，\x01",
            "正好碰到了各位游击士。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0xE, 215, 400)
    Sleep(400)

    ChrTalk(    #107
        0xE,
        "这是诺曼先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xE,
        (
            "你们一定在街头巷尾的\x01",
            "海报上见过他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1011F哦，是那位市长候选人啊。\x02\x03",

            "#1000F我是游击士\x01",
            "艾丝蒂尔·布莱特。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_197E")

    ChrTalk(    #110
        0x106,
        (
            "#050F我是她的同伴，\x01",
            "阿加特·科洛斯纳。\x02\x03",

            "请快告诉我们发生了什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C9")

    label("loc_197E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_19C9")

    ChrTalk(    #111
        0x103,
        (
            "#020F我是她的同伴，\x01",
            "雪拉扎德·哈维。\x02\x03",

            "请快告诉我们发生了什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C9")

    OP_8C(0xB, 180, 400)

    ChrTalk(    #112
        0xB,
        (
            "我们的工作人员德尔斯\x01",
            "受到了他人的暴力对待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        "也就是伤害案件。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1002F伤害案件……\x01",
            "这可不是闹着玩的。\x02\x03",

            "……受害者要不要紧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x1A, 400)
    Sleep(400)

    ChrTalk(    #115
        0xB,
        "嗯，他就在这里。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #116
        0xB,
        (
            "刚才还处于昏迷状态，\x01",
            "幸好没什么大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1007F啊……\x01",
            "那真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #118
        0x1A,
        "一点都不好哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x1A,
        (
            "头后面肿得那么厉害，\x01",
            "还阵阵地疼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#1004F啊，头后面……\x02\x03",

            "难道是被人从背后袭击了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1A,
        "嗯，而且还是突然地。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x1A,
        (
            "我当时正在阳台上休息，\x01",
            "突然有人从背后打了我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BCE")

    ChrTalk(    #123
        0x106,
        "#057F这可是恶性事件……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF8")

    label("loc_1BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1BF8")

    ChrTalk(    #124
        0x103,
        "#022F这可是相当恶性的事件……\x02",
    )

    CloseMessageWindow()

    label("loc_1BF8")


    ChrTalk(    #125
        0x101,
        "#1020F真、真狠啊～\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1C57")

    ChrTalk(    #126
        0x106,
        (
            "#050F事情是什么时候发生的？\x02\x03",

            "请仔细说说\x01",
            "前后过程。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9C")

    label("loc_1C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(    #127
        0x103,
        (
            "#022F事情是什么时候发生的？\x02\x03",

            "请把前后过程\x01",
            "也仔细说说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9C")


    ChrTalk(    #128
        0xE,
        "嗯，那是今天午饭后的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xE,
        (
            "我正和诺曼先生在大桥那边的\x01",
            "演说场地进行预练……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xE,
        (
            "这边的这位昆茨先生\x01",
            "正好来到了那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xE,
        (
            "他对诺曼先生说有\x01",
            "很重要的事要找他。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #132
        0x101,
        "#1002F……什么样的事？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #133
        0x14,
        (
            "我在波尔多斯先生的劝说下\x01",
            "前来为桥上的骚乱道歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x14,
        (
            "虽然不全都是我的错，\x01",
            "不过我确实煽动了人们的对立情绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1015F原来如此，你是来为\x01",
            "那次骚乱道歉的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xE,
        (
            "嗯，可是那个时候诺曼先生\x01",
            "还有事要处理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xE,
        (
            "所以我就让昆茨先生去\x01",
            "事务所等着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        (
            "然后我就把他\x01",
            "带到了这个房间。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #139
        0xB,
        (
            "不久之后\x01",
            "我返回了酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "和在房间前等着的海利欧\x01",
            "一起进入了事务所……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "然后就发现你们旁边的德尔斯\x01",
            "在阳台上昏过去了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #142
        0xE,
        "并且在那旁边……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x14, 400)

    def lambda_1F33():
        TurnDirection(0xB, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F33)

    def lambda_1F41():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1F41)
    OP_6D(-3080, 0, 79610, 1000)

    ChrTalk(    #143
        0xE,
        "站着这位昆茨先生。\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #144
        0x14,
        (
            "我说啊～为什么你们后来\x01",
            "就把我当成是犯人了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x14,
        (
            "我来到上阳台的时候\x01",
            "这家伙已经倒在那里了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "我明白昆茨先生的心情，\x01",
            "不过这么怀疑也是很正常的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "因为在这个房间里\x01",
            "除了你和德尔斯以外\x01",
            "没有别人了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #148
        0x101,
        "#1002F确实是这样？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #149
        0xE,
        (
            "把昆茨先生带来之后，\x01",
            "我就在门外守着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xE,
        (
            "当然在诺曼先生来之前\x01",
            "谁都不可能进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        "不管怎么看都只有他们两个人。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2122")
    TurnDirection(0x106, 0x14, 400)

    ChrTalk(    #152
        0x106,
        "#050F……确实是这样？\x02",
    )

    CloseMessageWindow()
    Jump("loc_214B")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_214B")
    TurnDirection(0x106, 0x14, 400)

    ChrTalk(    #153
        0x103,
        "#022F……确实是这样？\x02",
    )

    CloseMessageWindow()

    label("loc_214B")

    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x14, 0xF7, 400)

    ChrTalk(    #154
        0x14,
        (
            "这倒是事实……\x01",
            "不过就像我刚才说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x14,
        (
            "我来到阳台上的时候\x01",
            "德尔斯已经倒在那里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21F6")

    ChrTalk(    #156
        0x106,
        (
            "#052F就是说…\x02\x03",

            "在你来之前\x01",
            "案件已经发生了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222B")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_222B")

    ChrTalk(    #157
        0x103,
        (
            "#022F就是说\x02\x03",

            "在你来之前\x01",
            "案件已经发生了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222B")

    OP_62(0x14, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #158
        0x14,
        "嗯，就是这么回事！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x14,
        "呀～真是好沟通。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #160
        0x101,
        (
            "#1015F那就等于是说在你之前\x01",
            "已经有人来过这间房间了……\x02\x03",

            "#1002F……德尔斯先生，你还记得些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x1A,
        "印象中是有人来过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1A,
        (
            "可是进出事务所的人很多。\x01",
            "完全不会去注意是谁的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1007F嗯，这倒也是。\x01",
            "因为是选举事务所嘛。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_23F7")

    ChrTalk(    #164
        0x106,
        (
            "#053F……看来案件的焦点\x01",
            "已经显露出来了。\x02\x03",

            "这起案件的犯人\x01",
            "是下面两个人中的一个。\x02\x03",

            "#057F要么是这个大叔，要么是\x01",
            "之前来到房间的某个人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2487")

    label("loc_23F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2487")

    ChrTalk(    #165
        0x103,
        (
            "#026F……看来案件的焦点\x01",
            "已经显露出来了。\x02\x03",

            "这起案件的犯人\x01",
            "是下面两个人中的一个。\x02\x03",

            "#027F要么是昆茨先生，要么是\x01",
            "之前来到房间的某个人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2487")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #166
        0x101,
        (
            "#1002F接下来就看证据了……\x02\x03",

            "怎样？\x01",
            "现在就去打听情况？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2551")

    ChrTalk(    #167
        0x106,
        "#050F如果没什么其它情报的话。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Sleep(400)

    ChrTalk(    #168
        0x106,
        (
            "#050F……如果有什么在意的事情\x01",
            "就趁现在说出来吧。\x02\x03",

            "小事情也可以说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D3")

    label("loc_2551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_25D3")

    ChrTalk(    #169
        0x103,
        "#020F嗯，如果没什么其它情报的话。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Sleep(400)

    ChrTalk(    #170
        0x103,
        (
            "#020F……如果有什么在意的事情\x01",
            "就趁现在说出来吧。\x02\x03",

            "小事情也没关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D3")

    Sleep(400)
    TurnDirection(0xB, 0xF7, 400)

    ChrTalk(    #171
        0xB,
        "那么，我有一些话要说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xB,
        (
            "……我在观察案发后的房间时\x01",
            "发现了一件不可思议的事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #173
        0x101,
        "#1002F有被翻动过的痕迹？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        "不，正相反。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "不如说是感觉收拾得\x01",
            "比以前更干净了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #176
        0x101,
        "#1004F啊？怎么回事？\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #177
        0x104,
        (
            "#032F嗯，如果一定要解释的话\x01",
            "那就是为了消除翻动痕迹的伪装吧。\x02\x03",

            "当然，这种过度的行为\x01",
            "反而会招来怀疑。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #178
        0xB,
        "哟，这可是有价值的意见……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        "……对了，你是谁？\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x2B)
    Sleep(200)

    ChrTalk(    #180
        0x104,
        (
            "#035F呵呵，我等待这个问题很久了。\x02\x03",

            "我是漂泊的诗人兼天才演员……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #181
        0x101,
        (
            "#1002F不过，如果没有东西失窃的话,\x01",
            "伪装的说法很难成立哦。\x02\x03",

            "现在分析一堆理由\x01",
            "也不是办法。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2852")

    ChrTalk(    #182
        0x106,
        "#053F#2P嗯，我有同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2875")

    label("loc_2852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2875")

    ChrTalk(    #183
        0x103,
        "#026F#2P嗯，我有同感。\x02",
    )

    CloseMessageWindow()

    label("loc_2875")

    OP_62(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x104,
        (
            "#035F呵、呵呵……\x02\x03",

            "艾丝蒂尔……\x01",
            "比以前更厉害了呢。\x02\x03",

            "应该说不愧是从\x01",
            "卢·洛克尔受训回来的呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 400)

    ChrTalk(    #185
        0x105,
        "#045F奥、奥利维尔先生……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #186
        0x101,
        (
            "#1007F这种时候\x01",
            "最好不要理他。\x02\x03",

            "#1006F好了，如果没什么可以再问的\x01",
            "我们就快点去打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_29D6")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #187
        0x106,
        (
            "#052F#2P嗯、嗯……\x02\x03",

            "#053F（看来她已经很\x01",
            "  了解对付他的方法了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2F")

    label("loc_29D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2A2F")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #188
        0x103,
        (
            "#023F是、是啊……\x02\x03",

            "#026F（她也开始明白应该\x01",
            "  怎么对付奥利维尔了……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2F")


    ChrTalk(    #189
        0xB,
        (
            "那么，调查的事\x01",
            "也请多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A82")
    TurnDirection(0x106, 0xB, 400)

    ChrTalk(    #190
        0x106,
        "#050F结果出来后再来汇报。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAF")

    label("loc_2A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2AAF")
    TurnDirection(0x103, 0xB, 400)

    ChrTalk(    #191
        0x103,
        "#020F结果出来后再来汇报。\x02",
    )

    CloseMessageWindow()

    label("loc_2AAF")


    ChrTalk(    #192
        0xB,
        "嗯，我等着你们的好消息。\x02",
    )

    CloseMessageWindow()
    OP_51(0x18, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 65535)
    ClearChrFlags(0x104, 0x2)
    OP_43(0x104, 0x1, 0x1, 0x2A)
    Sleep(100)
    OP_43(0x101, 0x1, 0x1, 0x2A)
    OP_43(0x105, 0x1, 0x1, 0x2A)
    OP_43(0xF7, 0x1, 0x1, 0x2A)
    OP_69(0x18, 0x3E8)
    Sleep(1000)

    ChrTalk(    #193
        0x101,
        (
            "#1002F那么，我们应该从哪入手呢？\x01",
            "这座酒店相当大呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C03")

    ChrTalk(    #194
        0x106,
        (
            "#050F兵分两路行动比较好。\x02\x03",

            "你和公主一组。\x01",
            "我和这个家伙一组。\x02\x03",

            "他们两人现在也是协力人员。\x01",
            "要请他们帮忙工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C83")

    label("loc_2C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2C83")

    ChrTalk(    #195
        0x103,
        (
            "#020F兵分两路行动比较好。\x02\x03",

            "艾丝蒂尔和殿下一起。\x01",
            "我和奥利维尔搭档。\x02\x03",

            "他们两人现在也是协力人员，\x01",
            "要请他们帮忙工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C83")


    ChrTalk(    #196
        0x101,
        (
            "#1017F哦，这样啊……\x02\x03",

            "嗯，让我再次说一声拜托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x105,
        "#041F呵呵，彼此彼此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x104,
        "#031F呵呵，作为协力人员这是理所应当的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1019F啊，你还是恢复得\x01",
            "和以前一样快呢～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DC8")

    ChrTalk(    #200
        0x106,
        (
            "#050F听着，我们首先要\x01",
            "从收集嫌疑人的信息开始。\x02\x03",

            "对所有有关人员都问一次\x07\x04『关于昆茨』\x01",
            "\x07\x00应该能得到些什么。\x02\x03",

            "如果有眉目了\x01",
            "就到我这里来通知我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E67")

    label("loc_2DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2E67")

    ChrTalk(    #201
        0x103,
        (
            "#020F听着，我们首先要\x01",
            "从收集嫌疑人的信息开始。\x02\x03",

            "对所有有关人员都问一次\x07\x04『关于昆茨』\x01",
            "\x07\x00应该能得到些什么。\x02\x03",

            "如果有了犯人的眉目\x01",
            "就到我这里来通知我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E67")


    ChrTalk(    #202
        0x101,
        (
            "#1015F知道了犯人是谁\x01",
            "来报告就行了吧？\x02\x03",

            "#1006F……好。\x01",
            "那我们行动吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xE, -3880, 0, 83810, 180)
    SetChrPos(0xB, -430, 0, 80990, 225)
    SetChrPos(0x14, -2450, 0, 80960, 180)
    OP_4B(0xB, 0)
    OP_4B(0x14, 0)
    OP_4B(0xE, 0)
    OP_28(0x69, 0x4, 0x2)
    OP_28(0x69, 0x4, 0x4)
    OP_28(0x69, 0x4, 0x8)
    RemoveParty(0x3, 0xFF)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -1300, 0, 78180, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F46")
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -2430, 0, 79710, 0)
    Jump("loc_2F66")

    label("loc_2F46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2F66")
    RemoveParty(0x2, 0xFF)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -2430, 0, 79710, 0)

    label("loc_2F66")

    SetChrPos(0x101, -2160, 0, 77200, 205)
    SetChrPos(0x105, -2160, 0, 77200, 205)
    OP_30(0x0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMapFlags(0x1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x2)
    Return()

    # Function_4_1618 end

    def Function_5_2FCF(): pass

    label("Function_5_2FCF")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #203
        "\x18要询问什么？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "关于昆茨")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_306C")
    OP_CC(0x1, 0x0, "声响")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_306C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_30A1")
    OP_CC(0x1, 0x0, "发怒")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_30DC")
    OP_CC(0x1, 0x0, "关于海利欧")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_3111")
    OP_CC(0x1, 0x0, "午饭")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3111")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_3146")
    OP_CC(0x1, 0x0, "钟声")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_317F")
    OP_CC(0x1, 0x0, "收拾善后")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_317F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_31BA")
    OP_CC(0x1, 0x0, "关于贝尔夫")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_31BA")

    OP_CC(0x1, 0x0, "离开")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3202")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_3202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3226")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_3226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_324A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_326E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_326E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3292")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_3292")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_32B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32DA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_32DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32FE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3308")

    label("loc_32FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3308")

    Return()

    # Function_5_2FCF end

    def Function_6_3309(): pass

    label("Function_6_3309")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3336"),
        (1, "loc_3487"),
        (2, "loc_34B2"),
        (3, "loc_358B"),
        (4, "loc_36A6"),
        (5, "loc_3BC0"),
        (6, "loc_3D59"),
        (7, "loc_3DD6"),
        (SWITCH_DEFAULT, "loc_3E22"),
    )


    label("loc_3336")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_33A2")

    ChrTalk(    #204
        0xFE,
        (
            "昆茨先生来到酒店的时候\x01",
            "我正在前厅里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "不过总觉得那个人\x01",
            "看起来好像在生气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3484")

    label("loc_33A2")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #206
        0xFE,
        (
            "昆茨先生来到酒店的时候\x01",
            "我正在前厅里……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_340E")

    ChrTalk(    #207
        0xFE,
        (
            "不过总觉得那个人好像\x01",
            "生气了似的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3442")

    label("loc_340E")


    ChrTalk(    #208
        0xFE,
        (
            "不过总觉得那个人好像\x01",
            "\x07\x04『生气』\x07\x00了似的。\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_3442")


    ChrTalk(    #209
        0xFE,
        "我就觉得会出什么事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "果然不出我所料，发生了案件。\x02",
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x2)

    label("loc_3484")

    Jump("loc_3E25")

    label("loc_3487")

    OP_28(0x6A, 0x1, 0x80)

    ChrTalk(    #211
        0xFE,
        "声响啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "没什么印象。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E25")

    label("loc_34B2")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_351E")

    ChrTalk(    #213
        0xFE,
        (
            "我觉得昆茨先生\x01",
            "那时在生气哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "因为刚发生过\x01",
            "那起骚乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "生气也很正常。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3588")

    label("loc_351E")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #216
        0xFE,
        (
            "嗯，我觉得昆茨先生\x01",
            "那时在生气哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "不过，因为刚发生过\x01",
            "那起骚乱呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "生气也很正常。\x02",
    )

    CloseMessageWindow()

    label("loc_3588")

    Jump("loc_3E25")

    label("loc_358B")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3614")

    ChrTalk(    #219
        0xFE,
        "海利欧先生也受到了怀疑吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "嗯～我以前觉得他和\x01",
            "德尔斯先生关系很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "不过出人意料的是事实并非如此。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36A3")

    label("loc_3614")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #222
        0xFE,
        (
            "这次是海利欧先生\x01",
            "受到怀疑吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "确实在返回酒店的时候\x01",
            "海利欧先生看起来也不大高兴哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "嗯，一定是和昆茨\x01",
            "先生在一起的关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A3")

    Jump("loc_3E25")

    label("loc_36A6")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_3817")
    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #225
        0xFE,
        (
            "在１楼吃完午饭后，\x01",
            "就一直磨磨蹭蹭地待在地下室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "真、真的哦。\x01",
            "我没必要撒谎吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "不、不过。\x01",
            "老爸那家伙也很狡猾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "让我们吃普通的东西，\x01",
            "自己一个人吃特制的什锦饭。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3814")
    OP_A2(0xB)

    ChrTalk(    #229
        0x101,
        "#1015F咦？可是……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #230
        0xFE,
        "啊啊！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #231
        0xFE,
        "这、这次又怎么了？\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_3814")

    Jump("loc_3BBD")

    label("loc_3817")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3908")
    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #232
        0xFE,
        "午饭是在１楼的前厅吃的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "不过，老爸那家伙也很狡猾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "让我们吃普通的东西，\x01",
            "自己一个人吃特制的什锦饭。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3905")
    OP_A2(0xB)

    ChrTalk(    #235
        0x101,
        "#1015F咦？可是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #236
        0xFE,
        "你、你怎么那副怪表情……\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_3905")

    Jump("loc_3BBD")

    label("loc_3908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_39F3")

    ChrTalk(    #237
        0xFE,
        "午饭是在１楼的前厅吃的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "不过，老爸那家伙也很狡猾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "让我们吃普通的东西，\x01",
            "自己一个人吃特制的什锦饭。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39F0")
    OP_A2(0xB)

    ChrTalk(    #240
        0x101,
        "#1015F咦？可是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #241
        0xFE,
        "你、你怎么那副怪表情……\x02",
    )

    CloseMessageWindow()
    Call(1, 8)

    label("loc_39F0")

    Jump("loc_3BBD")

    label("loc_39F3")

    OP_28(0x6A, 0x1, 0x1)

    ChrTalk(    #242
        0xFE,
        "嗯，午餐是什锦饭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "我一个人在前厅吃的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "和老爸在一个房间吃饭\x01",
            "总感觉很尴尬……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "不过，老爸那家伙也很狡猾啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "让我们吃普通的东西，\x01",
            "他自己一个人吃特制的什锦饭哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        (
            "#1016F啊哈哈，是这样呀。\x02\x03",

            "有那么不一样吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #248
        0xFE,
        (
            "嗯，天差地别呢。\x01",
            "特制的里面放了很多很多的虾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "老爸好像没食欲，\x01",
            "就留下了不少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "多可惜啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BBD")
    OP_A2(0xB)

    ChrTalk(    #251
        0x101,
        "#1015F咦？可是……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #252
        0xFE,
        "你、你怎么那副怪表情……\x02",
    )

    CloseMessageWindow()
    Call(1, 8)
    Jump("loc_3BBD")

    label("loc_3BBD")

    Jump("loc_3E25")

    label("loc_3BC0")

    OP_28(0x6A, 0x1, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x9), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3C8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_3C33")
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #253
        0xFE,
        (
            "我、我待在地下室，\x01",
            "没听到什么钟声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "真、真的哦。\x01",
            "我没必要撒谎吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C8C")

    label("loc_3C33")

    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #255
        0xFE,
        "是吗，桥上的钟已经响过了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "因为我在酒店的地下室，\x01",
            "所以一点也没注意到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8C")

    Jump("loc_3D56")

    label("loc_3C8F")

    RunExpression(0x9, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_3CF9")
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #257
        0xFE,
        (
            "我、我待在地下室，\x01",
            "没听到什么钟声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "真、真的哦。\x01",
            "我没必要撒谎吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D56")

    label("loc_3CF9")

    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #259
        0xFE,
        "咦，有钟声响过？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "因为我在酒店的地下室，\x01",
            "没怎么注意。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D56")
    Call(1, 7)

    label("loc_3D56")

    Jump("loc_3E25")

    label("loc_3D59")

    OP_28(0x6A, 0x1, 0x80)
    OP_28(0x6A, 0x1, 0x2)

    ChrTalk(    #261
        0xFE,
        (
            "收拾事务所的餐具？\x01",
            "我可没做那么麻烦的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "吃了饭以后\x01",
            "我在酒店的地下室发呆。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD3")
    Call(1, 7)

    label("loc_3DD3")

    Jump("loc_3E25")

    label("loc_3DD6")

    OP_28(0x6A, 0x1, 0x80)

    ChrTalk(    #263
        0xFE,
        (
            "我、我都说了\x01",
            "钟响的时候我在地下室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "午饭后一直在地下哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E25")

    label("loc_3E22")

    Jump("loc_3E25")

    label("loc_3E25")

    Return()

    # Function_6_3309 end

    def Function_7_3E26(): pass

    label("Function_7_3E26")

    OP_28(0x69, 0x1, 0x2000)

    ChrTalk(    #265
        0x101,
        (
            "#1019F……………………………………\x02\x03",

            "……你真的一直在地下室？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #266
        0xFE,
        "咦！？为、为什么这么问？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        (
            "#1002F有一个人在钟刚响的时候\x01",
            "正好去了地下室哦。\x02\x03",

            "根据那个人的证词\x01",
            "地下室没有人在。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #268
        0xFE,
        "不、不可能的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "因、因为我一直\x01",
            "待在那里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x105,
        "#042F（没不在场证明呢……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #271
        0x101,
        (
            "#1002F（谨慎起见去问问\x07\x04『关于贝尔夫』\x01",
            "\x07\x00会比较好吧。）\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()
    Return()

    # Function_7_3E26 end

    def Function_8_3FBE(): pass

    label("Function_8_3FBE")

    OP_28(0x69, 0x1, 0x1000)

    ChrTalk(    #272
        0xFE,
        "我说错了什么吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_40C1")

    ChrTalk(    #273
        0x101,
        (
            "#1015F不，我只是有点在意……\x02\x03",

            "#1002F……我说，贝尔夫。\x02\x03",

            "听说你的午饭\x01",
            "是在１楼吃的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #274
        0xFE,
        "嗯、嗯……是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1015F可诺曼先生\x01",
            "是在２楼吃的吧。\x02\x03",

            "在１楼的你，\x01",
            "为什么会知道诺曼\x01",
            "吃的是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A1")

    label("loc_40C1")


    ChrTalk(    #277
        0x101,
        (
            "#1015F不，我只是有点在意……\x02\x03",

            "#1002F……我说，贝尔夫先生。\x02\x03",

            "你上回说了是\x01",
            "特制什锦饭吧。\x02\x03",

            "还有你也说过诺曼先生一个人\x01",
            "吃那个很狡猾。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #278
        0xFE,
        (
            "啊、啊啊……\x01",
            "我好像没记错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "有什么问题吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1015F嗯，那你怎么会\x01",
            "知道那些的呢……\x02\x03",

            "……我们实在是想不通。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "这，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#1010F你说你在１楼的前厅\x01",
            "吃的午饭是吧。\x02\x03",

            "而诺曼先生是在２楼的\x01",
            "事务所吃的什锦饭。\x02\x03",

            "#1002F在这种情况下\x01",
            "你那番话是不是有点奇怪？\x02\x03",

            "在１楼的你，\x01",
            "为什么会知道诺曼先生\x01",
            "吃的是什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A1")


    ChrTalk(    #284
        0xFE,
        "那、那又怎么样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "当然是后来看到的了……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #286
        0xFE,
        (
            "………………………………\x01",
            "…………啊………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x101,
        "#1019F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x105,
        "#044F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #289
        0xFE,
        (
            "唔、唔……\x01",
            "抱歉我说错了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "嗯，其实那些我是\x01",
            "听说的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "很、很遗憾,\x01",
            "我忘了是谁告诉我的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "接、接下来你们\x01",
            "调查一下不就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        "#1007F（真、真的很可疑。）\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_8_3FBE end

    def Function_9_442A(): pass

    label("Function_9_442A")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4457"),
        (1, "loc_44B8"),
        (2, "loc_44F6"),
        (3, "loc_45A9"),
        (4, "loc_4B2D"),
        (5, "loc_4BF4"),
        (6, "loc_4EBE"),
        (7, "loc_4F0D"),
        (SWITCH_DEFAULT, "loc_4FE4"),
    )


    label("loc_4457")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #294
        0xA,
        (
            "昆茨先生很少\x01",
            "来我们酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xA,
        (
            "大多数情况下都是因为\x01",
            "工作上的集会来租用我们的房间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE7")

    label("loc_44B8")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #296
        0xA,
        "哦，声响啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xA,
        (
            "不好意思，\x01",
            "我什么也没听见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE7")

    label("loc_44F6")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4550")

    ChrTalk(    #298
        0xA,
        (
            "昆茨先生的样子\x01",
            "和平时并没有不同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xA,
        (
            "怎么也看不出\x01",
            "是在生气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A6")

    label("loc_4550")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #300
        0xA,
        (
            "所以，我无法赞同\x01",
            "那一位的观点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xA,
        (
            "昆茨先生的样子\x01",
            "和平时并没有不同。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A6")

    Jump("loc_4FE7")

    label("loc_45A9")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_463C")

    ChrTalk(    #302
        0xA,
        (
            "非常抱歉我没有\x01",
            "把该说的事情说出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xA,
        (
            "可是，海利欧先生\x01",
            "不可能是犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xA,
        (
            "那位先生怎么会犯罪呢……\x01",
            "我实在无法想象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2A")

    label("loc_463C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_4A4E")
    OP_28(0x69, 0x1, 0x10)
    OP_A2(0xE)
    OP_A2(0xF)

    ChrTalk(    #305
        0xA,
        (
            "您、您还在怀疑\x01",
            "海利欧先生吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "海利欧先生是诚实的人。\x01",
            "不可能是犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xA,
        (
            "所以，那位先生\x01",
            "不可能是犯人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        (
            "#1002F？？？\x02\x03",

            "怎、怎么了？\x01",
            "我好像觉得你有点顾虑？\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x17, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4762")
    OP_4A(0x15, 0)

    ChrTalk(    #309
        0x15,
        (
            "#057F有什么瞒着我们的事情，\x01",
            "还是坦白比较好。\x02\x03",

            "包庇的心情\x01",
            "经常是会害人的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BC")

    label("loc_4762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_47BC")
    OP_4A(0x16, 0)

    ChrTalk(    #310
        0x16,
        (
            "#027F有什么瞒着我们的事情，\x01",
            "还是老实说比较好哦。\x02\x03",

            "包庇别人往往\x01",
            "会害人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BC")


    ChrTalk(    #311
        0xA,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xA,
        "对、对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#1002F你想说了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xA,
        "是，其实………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xA,
        (
            "我看见了。\x01",
            "海利欧先生上了２楼。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_486B")

    ChrTalk(    #316
        0x15,
        "#057F……那是什么时候？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x15, 400)
    Jump("loc_4896")

    label("loc_486B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4896")

    ChrTalk(    #317
        0x16,
        "#022F……那是什么时候？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x16, 400)

    label("loc_4896")

    Sleep(400)

    ChrTalk(    #318
        0xA,
        "\x07\x04『午餐』\x07\x00刚吃完之后。\x02",
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #319
        0xA,
        (
            "海利欧先生和诺曼先生\x01",
            "一起出了门……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xA,
        (
            "可是没过多久，\x01",
            "海利欧先生一个人回来\x01",
            "上了２楼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#1002F这是重要的证词……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_49A2")
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #322
        0x15,
        (
            "#050F艾丝蒂尔你们去\x01",
            "调查一下该证词所说的事情。\x02\x03",

            "我们在这里\x01",
            "再拖延一些时间。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x15, 400)
    Jump("loc_4A08")

    label("loc_49A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4A08")
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(    #323
        0x16,
        (
            "#022F艾丝蒂尔你们去\x01",
            "调查一下该证词所说的事情。\x02\x03",

            "我们在这里\x01",
            "再拖延一些时间。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x16, 400)

    label("loc_4A08")


    ChrTalk(    #324
        0x101,
        "#1002F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x17, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4A39")
    OP_4B(0x15, 0)
    TurnDirection(0x15, 0xA, 0)
    Jump("loc_4A4B")

    label("loc_4A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4A4B")
    OP_4B(0x16, 0)
    TurnDirection(0x16, 0xA, 0)

    label("loc_4A4B")

    Jump("loc_4B2A")

    label("loc_4A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD4")
    OP_28(0x6A, 0x1, 0x8)

    ChrTalk(    #325
        0xA,
        (
            "连海利欧先生\x01",
            "你们也怀疑吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xA,
        (
            "他可不是一个\x01",
            "会动用暴力的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xA,
        (
            "所以，海利欧先生也\x01",
            "不可能是犯人的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B2A")

    label("loc_4AD4")


    ChrTalk(    #328
        0xA,
        (
            "海利欧先生是诚实的人。\x01",
            "不可能是犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xA,
        (
            "所以，海利欧先生\x01",
            "怎么可能是犯人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2A")

    Jump("loc_4FE7")

    label("loc_4B2D")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4B99")

    ChrTalk(    #330
        0xA,
        (
            "午饭后诺曼先生\x01",
            "和海利欧先生一同外出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xA,
        (
            "然后海利欧先生\x01",
            "一个人回来上了２楼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF1")

    label("loc_4B99")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #332
        0xA,
        (
            "午饭是从拉旺塔尔\x01",
            "叫的外卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xA,
        (
            "大家是在令人怀念又怀念的\x01",
            "地方用了餐呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF1")

    Jump("loc_4FE7")

    label("loc_4BF4")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_4C5C")

    ChrTalk(    #334
        0xA,
        (
            "中午桥上的钟响的时候\x01",
            "我正在整理餐具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xA,
        (
            "不知道是谁把事务所的餐具\x01",
            "收拾好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EBB")

    label("loc_4C5C")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_28(0x69, 0x1, 0x800)

    ChrTalk(    #336
        0xA,
        "中午桥上的钟响的时候？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xA,
        (
            "嗯，我正在\x01",
            "做着客厅的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xA,
        (
            "结束以后\x01",
            "我就去整理了餐具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xA,
        (
            "不知道是谁把事务所的餐具\x01",
            "收拾好了，所以\x01",
            "我的工作也就很快做完了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #340
        0x105,
        "#044F事务所的餐具被人收拾好了……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x101,
        (
            "#1004F也、也就是说……\x02\x03",

            "午饭后有人\x01",
            "去了事务所！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #342
        0xA,
        "是的，如您所说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xA,
        (
            "在准备客厅的时候，\x07\x04\x01",
            "『收拾善后』\x07\x00的事有人替我做了……\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #344
        0xA,
        (
            "等我发现的时候\x01",
            "餐具已经堆放在前台了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xA,
        (
            "不过说起来，那位好心人\x01",
            "究竟是哪位客人呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xA,
        (
            "不好意思，我也\x01",
            "不知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#1007F是、是吗，真遗憾。\x02\x03",

            "还是我们自己去\x01",
            "问一遍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBB")

    Jump("loc_4FE7")

    label("loc_4EBE")

    OP_28(0x6A, 0x1, 0x200)

    ChrTalk(    #348
        0xA,
        (
            "我也不知道是\x01",
            "哪一位收拾的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xA,
        (
            "应该是在我准备客厅时\x01",
            "收拾的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE7")

    label("loc_4F0D")

    OP_28(0x6A, 0x1, 0x200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_4F7F")

    ChrTalk(    #350
        0xA,
        "贝尔夫先生吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xA,
        (
            "钟响的时候\x01",
            "没看见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xA,
        (
            "在我整理好餐具的时候\x01",
            "他还在前厅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE1")

    label("loc_4F7F")

    RunExpression(0x8, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #353
        0xA,
        "贝尔夫先生吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xA,
        (
            "不知道，钟响的时候\x01",
            "没看见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xA,
        (
            "我正好在做\x01",
            "客房的准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE1")

    Jump("loc_4FE7")

    label("loc_4FE4")

    Jump("loc_4FE7")

    label("loc_4FE7")

    Return()

    # Function_9_442A end

    def Function_10_4FE8(): pass

    label("Function_10_4FE8")

    TalkBegin(0xFE)
    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5018"),
        (1, "loc_5169"),
        (2, "loc_52D9"),
        (3, "loc_54BD"),
        (4, "loc_55A6"),
        (5, "loc_560D"),
        (6, "loc_5766"),
        (7, "loc_57B8"),
        (SWITCH_DEFAULT, "loc_5801"),
    )


    label("loc_5018")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5073")

    ChrTalk(    #356
        0xFE,
        (
            "如果我们吵架的话，\x01",
            "应该会有什么响声的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        "没人说过这个吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_5073")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #358
        0xFE,
        (
            "我说了好多次了，\x01",
            "我只发现了德尔斯。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_50EE")

    ChrTalk(    #359
        0xFE,
        (
            "如果我们吵架的话，\x01",
            "响声总会有的吧，\x01",
            "没人说过这个吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5135")

    label("loc_50EE")


    ChrTalk(    #360
        0xFE,
        (
            "如果我们吵架的话，\x01",
            "\x07\x04『响声』\x07\x00总会有的吧。\x01",
            "没人说过这个吧？\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_5135")


    ChrTalk(    #361
        0xFE,
        (
            "当然了，我是很有礼貌地\x01",
            "坐在沙发上的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x1)

    label("loc_5166")

    Jump("loc_5804")

    label("loc_5169")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_51D5")

    ChrTalk(    #362
        0xFE,
        (
            "我在这个房间的时候\x01",
            "应该会有什么响声的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "是不是作证的那家伙的\x01",
            "耳朵有问题？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52D6")

    label("loc_51D5")


    ChrTalk(    #364
        0xFE,
        (
            "如果我和德尔斯争吵过的话\x01",
            "应该会有什么响声的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_52D6")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #365
        0x101,
        (
            "#1015F可是说到巨大的响声，\x01",
            "有人可以作证呢。\x02\x03",

            "还有人说有某种碰撞声\x01",
            "从阳台传来……\x02\x03",

            "#1002F……你对那个声音没印象吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        "某种大的碰撞声？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        (
            "不，不可能的。\x01",
            "我没听到过那种声音。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52D6")

    Jump("loc_5804")

    label("loc_52D9")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5348")

    ChrTalk(    #368
        0xFE,
        "我没有生过气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        (
            "再说我这次是\x01",
            "代表我的阵营来道歉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "怎么可能怒气冲冲的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_54BA")

    label("loc_5348")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #371
        0xFE,
        (
            "说我生气了？\x01",
            "说话真不负责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        (
            "要这么说的话海利欧\x01",
            "那家伙比我态度还差呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        (
            "那家伙一看到我\x01",
            "就露出厌恶的神情。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_5416")

    ChrTalk(    #374
        0xFE,
        (
            "关于海利欧的事你们去打听一下吧。\x01",
            "肯定能发现蛛丝马迹的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5460")

    label("loc_5416")


    ChrTalk(    #375
        0xFE,
        (
            "\x07\x04『关于海利欧』\x07\x00的事你们去打听一下吧。\x01",
            "肯定能发现蛛丝马迹的。\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    label("loc_5460")


    ChrTalk(    #376
        0xFE,
        (
            "那家伙和德尔斯是争夺\x01",
            "诺曼阵营二号人物的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        (
            "一定是彼此不合就\x01",
            "打起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x8)

    label("loc_54BA")

    Jump("loc_5804")

    label("loc_54BD")

    OP_28(0x6A, 0x1, 0x1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5527")

    ChrTalk(    #378
        0xFE,
        (
            "海利欧和德尔斯是争夺\x01",
            "诺曼阵营二号人物的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        (
            "一定是彼此不合就\x01",
            "打起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55A3")

    label("loc_5527")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #380
        0xFE,
        "海利欧也有动机吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "那家伙和德尔斯是争夺\x01",
            "诺曼阵营二号人物的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "一定是彼此不合就\x01",
            "打起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6A, 0x1, 0x2000)

    label("loc_55A3")

    Jump("loc_5804")

    label("loc_55A6")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #383
        0xFE,
        (
            "哟，原来是从拉旺塔尔\x01",
            "叫来的外卖吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "还真有闲情逸致啊。\x01",
            "下回我也去拜托波尔多斯先生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5804")

    label("loc_560D")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #385
        0xFE,
        "拉升大桥时的钟声吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "哦，那时候我正好\x01",
            "急着过桥呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "所以就偶然遇到了\x01",
            "在桥边的诺曼先生他们。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5763")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5733")
    OP_28(0x69, 0x1, 0x100)

    ChrTalk(    #388
        0x101,
        (
            "#1019F唔……就是说……\x02\x03",

            "昆茨先生和\x01",
            "那个声音没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x105,
        (
            "#047F根据证词，响声出现在\x01",
            "钟声刚结束之后……\x02\x03",

            "#042F据他本人所说，\x01",
            "是这样的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5763")

    label("loc_5733")


    ChrTalk(    #390
        0x101,
        (
            "#1002F这样啊……\x02\x03",

            "和诺曼先生的证词一样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5763")

    Jump("loc_5804")

    label("loc_5766")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #391
        0xFE,
        "在找收拾餐具的人？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xFE,
        (
            "算了，不管你们怎么做，\x01",
            "快点证明我的无罪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5804")

    label("loc_57B8")

    OP_28(0x6A, 0x1, 0x1000)

    ChrTalk(    #393
        0xFE,
        (
            "钟响的时候\x01",
            "贝尔夫在什么地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0xFE,
        (
            "我怎么可能\x01",
            "知道那种事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5804")

    label("loc_5801")

    Jump("loc_5804")

    label("loc_5804")

    TalkEnd(0xFE)
    Return()

    # Function_10_4FE8 end

    def Function_11_5808(): pass

    label("Function_11_5808")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_5857")

    ChrTalk(    #395
        0xFE,
        (
            "#030F呼，快要接近尾声了。\x02\x03",

            "那么，快点解决了\x01",
            "举杯庆祝吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E28")

    label("loc_5857")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_5942")
    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_58C7")

    ChrTalk(    #396
        0xFE,
        (
            "#035F我从小一直在城市里，\x01",
            "站久了受不了。\x02\x03",

            "呵呵，就像美丽的花朵\x01",
            "容易凋谢一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_593F")

    label("loc_58C7")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #397
        0xFE,
        (
            "#034F呼，开始有点累了。\x02\x03",

            "我从小一直在城市里，\x01",
            "站久了受不了。\x02\x03",

            "#037F呵呵，就像美丽的花朵\x01",
            "容易凋谢一样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_593F")

    Jump("loc_5E28")

    label("loc_5942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_5A1D")
    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_59BB")

    ChrTalk(    #398
        0xFE,
        (
            "#035F钟的事情我以前\x01",
            "在旅游向导里读过。\x02\x03",

            "想法是很好，\x01",
            "不过如果用长笛代替钟\x01",
            "的话应该更好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A1A")

    label("loc_59BB")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #399
        0xFE,
        (
            "#030F钟就是指\x01",
            "那座大桥上的钟吗？\x02\x03",

            "那个以前\x01",
            "在书里读过。\x02\x03",

            "哦，那本书叫旅游向导。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A1A")

    Jump("loc_5E28")

    label("loc_5A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_5B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_5A8F")

    ChrTalk(    #400
        0xFE,
        (
            "#031F呵呵，我就觉得有点奇怪，\x01",
            "果然是这样啊。\x02\x03",

            "想不到连人心都能读懂……\x01",
            "我还真是个罪人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B49")

    label("loc_5A8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5ADD")

    ChrTalk(    #401
        0xFE,
        (
            "#030F我查到了今天的\x01",
            "午饭菜谱……\x02\x03",

            "呼，果然冷盘是个问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B49")

    label("loc_5ADD")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #402
        0xFE,
        (
            "#030F我查到了今天的\x01",
            "午饭菜谱……\x02\x03",

            "#035F呼，果然冷盘是个问题。\x02\x03",

            "真希望能拿出点\x01",
            "更精致的菜肴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B49")

    Jump("loc_5E28")

    label("loc_5B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_5BC0")

    ChrTalk(    #403
        0xFE,
        (
            "#032F呼，总觉得这个\x01",
            "在前台的人样子有点古怪。\x02\x03",

            "如果用逼问让他动摇的话,\x01",
            "说不定会得到意外的情报哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E28")

    label("loc_5BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_5D0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5C33")

    ChrTalk(    #404
        0xFE,
        (
            "#034F呼，真服了。\x02\x03",

            "从刚才起阿加特\x01",
            "就对我不理不睬。\x02\x03",

            "#032F唔，要不要我在他\x01",
            "耳边吹口气呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C96")

    label("loc_5C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5C96")

    ChrTalk(    #405
        0xFE,
        (
            "#034F呼，真服了。\x02\x03",

            "从刚才起雪拉\x01",
            "就对我不理不睬。\x02\x03",

            "#032F唔，要不要我在她\x01",
            "耳边吹口气呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C96")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5CA6")
    Jump("loc_5D07")

    label("loc_5CA6")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #406
        0x101,
        (
            "#1015F我不会阻止你……\x02\x03",

            "#1007F不过我觉得那么做的话，\x01",
            "伤害事件就会变成杀人事件了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D07")

    Jump("loc_5E28")

    label("loc_5D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5D69")

    ChrTalk(    #407
        0xFE,
        (
            "#030F嗯，从这里看晚霞的话\x01",
            "一定非常美。\x02\x03",

            "有时间的话我真想\x01",
            "悠闲地多逗留一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E28")

    label("loc_5D69")

    Jc((scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5DB1")

    ChrTalk(    #408
        0xFE,
        (
            "#031F呵呵，我那华丽的语言艺术\x01",
            "终于可以大显神威了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E28")

    label("loc_5DB1")

    RunExpression(0xA, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #409
        0xFE,
        (
            "#031F呵呵，我那华丽的语言艺术\x01",
            "终于可以大显神威了。\x02\x03",

            "你们就见识一下我那独占了\x01",
            "社交界话题的玫瑰色语言吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E28")

    TalkEnd(0xFE)
    Return()

    # Function_11_5808 end

    def Function_12_5E2C(): pass

    label("Function_12_5E2C")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5E59"),
        (1, "loc_5F26"),
        (2, "loc_5FA4"),
        (3, "loc_600E"),
        (4, "loc_60EF"),
        (5, "loc_63F0"),
        (6, "loc_66C7"),
        (7, "loc_69C7"),
        (SWITCH_DEFAULT, "loc_6A49"),
    )


    label("loc_5E59")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_5EA8")

    ChrTalk(    #410
        0xFE,
        (
            "昆茨站在倒地的\x01",
            "德尔斯旁边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xFE,
        "他的脸色很吃惊哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F23")

    label("loc_5EA8")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #412
        0xFE,
        (
            "昆茨站在倒地的\x01",
            "德尔斯旁边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xFE,
        (
            "看到我们以后\x01",
            "他好像很吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0xFE,
        (
            "虽然没有兴奋的感觉，\x01",
            "不过总之表情很惊讶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F23")

    Jump("loc_6A4C")

    label("loc_5F26")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #415
        0xFE,
        (
            "就像昆茨说的那样，\x01",
            "一点也没听见有什么响声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0xFE,
        (
            "我那时正在前厅，\x01",
            "如果有成年人上楼去的话，\x01",
            "当然能听到些声音的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A4C")

    label("loc_5FA4")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #417
        0xFE,
        (
            "在大桥边遇到的时候\x01",
            "没发现他有在生气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0xFE,
        (
            "当然，说不定是在\x01",
            "领他去酒店的时候\x01",
            "发生了什么吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A4C")

    label("loc_600E")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_607C")

    ChrTalk(    #419
        0xFE,
        (
            "争夺二号人物位置这种\x01",
            "说法只不过是臆测而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xFE,
        (
            "我想诸位也不会相信\x01",
            "这种传言的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60EC")

    label("loc_607C")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #421
        0xFE,
        (
            "怀疑海利欧是无法\x01",
            "令人信服的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0xFE,
        (
            "再说他为什么要\x01",
            "伤害自己的同事德尔斯呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0xFE,
        "有什么动机吗？\x02",
    )

    CloseMessageWindow()

    label("loc_60EC")

    Jump("loc_6A4C")

    label("loc_60EF")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6161")

    ChrTalk(    #424
        0xFE,
        (
            "午饭后，我和海利欧\x01",
            "去演说现场进行了预练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xFE,
        (
            "海利欧因为有事，\x01",
            "后来才在那里和我会合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63ED")

    label("loc_6161")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #426
        0xFE,
        (
            "嗯，今天的午饭\x01",
            "是从拉旺塔尔叫的外卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0xFE,
        (
            "总是同样的菜谱的话\x01",
            "工作人员也会吃腻的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1011F哟，还真是用心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x105,
        (
            "#040F或者说政治家的工作\x01",
            "就是这些事情吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #430
        0xFE,
        "哈哈，你说的很有道理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0xFE,
        (
            "无时无刻不在用心，\x01",
            "脑细胞都被大量杀伤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x105,
        "#045F好、好像很可怜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1007F确、确实……\x01",
            "做到这种程度真不容易。\x02\x03",

            "#1002F这些先说到这里，诺曼先生。\x02\x03",

            "你午饭后在干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #434
        0xFE,
        (
            "哦，我和海利欧\x01",
            "为了去演说现场进行预练而出了门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xFE,
        (
            "海利欧因为有其它事\x01",
            "而和我约好在目的地会合的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x101,
        (
            "#1000F午饭后立即外出，\x01",
            "然后在外面和海利欧先生会合了是吗？\x02\x03",

            "嗯，只要确认了这一点就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        "能帮上你们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xFE,
        "那么，接下来还要继续拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_63ED")

    Jump("loc_6A4C")

    label("loc_63F0")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6447")

    ChrTalk(    #439
        0xFE,
        "桥上的钟响了的时候吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0xFE,
        (
            "我和海利欧一起在\x01",
            "演说现场预练。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66C4")

    label("loc_6447")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #441
        0xFE,
        "桥上的钟响了的时候吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "我和海利欧一起在\x01",
            "演说现场预练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x101,
        "#1002F海利欧先生也在那里？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #444
        0xFE,
        "嗯，他那时已经来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0xFE,
        (
            "正好在钟响的时候\x01",
            "那个昆茨来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0xFE,
        (
            "我拜托海利欧把他带去酒店，\x01",
            "所以应该不会记错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x101,
        "#1015F是吗，那应该不会错了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66C4")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #448
        0x105,
        (
            "#043F这么说的话，艾丝蒂尔……\x02\x03",

            "穆拉德先生听到的响声\x01",
            "看来和海利欧先生没关系了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #449
        0x101,
        (
            "#1015F嗯，不光是海利欧先生，\x01",
            "和昆茨先生也变得无关了呢。\x02\x03",

            "穆拉德先生听到响声\x01",
            "是在钟刚响之后……\x02\x03",

            "不过那时两个人都和\x01",
            "诺曼先生在一起。\x02\x03",

            "#1002F也就是说，那个响声的制造者既不是\x01",
            "海利欧先生也不是昆茨先生……\x02\x03",

            "两个人作为犯人的可能性\x01",
            "这样一来就相当低了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x400)

    label("loc_66C4")

    Jump("loc_6A4C")

    label("loc_66C7")

    OP_28(0x6A, 0x1, 0x800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68BC")
    OP_28(0x6A, 0x1, 0x4)

    ChrTalk(    #450
        0xFE,
        (
            "那么，到底\x01",
            "是谁做的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "在我们出门的期间\x01",
            "似乎有人收拾了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x101,
        (
            "#1015F这么说……\x01",
            "诺曼先生也不知道呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #453
        0xFE,
        "嗯，很遗憾……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0xFE,
        "可是，虽然不知道是谁……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        (
            "不过我可能给那个好人\x01",
            "留下了不好的回忆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x101,
        "#1011F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x105,
        "#043F出什么事了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #458
        0xFE,
        (
            "嗯，其实最近……\x01",
            "我一直没有食欲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xFE,
        (
            "中午的什锦饭\x01",
            "我也剩下了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        (
            "难得亚内斯特瞒着大家\x01",
            "为我特别订了特制什锦饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xFE,
        "……哎呀，真是见笑了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x101,
        (
            "#1007F是、是吗……\x02\x03",

            "呼，参加选举也真不容易。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69C4")

    label("loc_68BC")


    ChrTalk(    #463
        0xFE,
        (
            "在我们出门的期间\x01",
            "似乎有人收拾了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "可是，我竟然会\x01",
            "做出这么让人见笑的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "难得亚内斯特秘密地\x01",
            "为我特别订了特制什锦饭……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xFE,
        (
            "结果因为提不起食欲\x01",
            "剩下了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "不好意思，请你们\x01",
            "不要告诉大家这件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xFE,
        (
            "我不想惹上『健康问题』\x01",
            "之类的不必要麻烦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69C4")

    Jump("loc_6A4C")

    label("loc_69C7")

    OP_28(0x6A, 0x1, 0x800)

    ChrTalk(    #469
        0xFE,
        (
            "唔，桥上的钟响时\x01",
            "我儿子所在的地点是个疑点？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0xFE,
        (
            "如果有合理的嫌疑\x01",
            "就不用顾及我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "拘捕贝尔夫，\x01",
            "审讯他也没关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A4C")

    label("loc_6A49")

    Jump("loc_6A4C")

    label("loc_6A4C")

    Return()

    # Function_12_5E2C end

    def Function_13_6A4D(): pass

    label("Function_13_6A4D")

    Call(1, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A7A"),
        (1, "loc_6B35"),
        (2, "loc_6C08"),
        (3, "loc_6C35"),
        (4, "loc_6D1A"),
        (5, "loc_6D5A"),
        (6, "loc_6E33"),
        (7, "loc_6F4E"),
        (SWITCH_DEFAULT, "loc_700B"),
    )


    label("loc_6A7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6AD6")

    ChrTalk(    #472
        0xFE,
        (
            "呼，如果我看到犯人的话\x01",
            "就能帮上你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        (
            "好痛……\x01",
            "头还是阵阵地疼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B32")

    label("loc_6AD6")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #474
        0xFE,
        (
            "一瞬间我就昏过去了，\x01",
            "所以没看见犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0xFE,
        (
            "如果看上一眼的话\x01",
            "就能帮上你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B32")

    Jump("loc_700E")

    label("loc_6B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6B9D")

    ChrTalk(    #476
        0xFE,
        (
            "如果说声响的话，\x01",
            "那就是我被袭击时的声音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xFE,
        (
            "因为那是响彻头脑的\x01",
            "可怕冲击声啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C05")

    label("loc_6B9D")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #478
        0xFE,
        "声响吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0xFE,
        (
            "啊，那个应该\x01",
            "是我被袭击时的声音了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0xFE,
        (
            "因为那是响彻头脑的\x01",
            "可怕冲击。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C05")

    Jump("loc_700E")

    label("loc_6C08")


    ChrTalk(    #481
        0xFE,
        "呼，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xFE,
        "问我我也不知道啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_700E")

    label("loc_6C35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6C84")

    ChrTalk(    #483
        0xFE,
        (
            "我甚至可以保证\x01",
            "海利欧不是犯人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0xFE,
        "因为他完全没有动机。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D17")

    label("loc_6C84")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #485
        0xFE,
        (
            "海利欧不可能是犯人。\x01",
            "这一点我可以保证啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0xFE,
        (
            "我们没什么过节，\x01",
            "而且生意上还有合作关系！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0xFE,
        (
            "啊，好痛……\x01",
            "因、因为太兴奋了头又……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D17")

    Jump("loc_700E")

    label("loc_6D1A")


    ChrTalk(    #488
        0xFE,
        (
            "是的，饭菜是从\x01",
            "拉旺塔尔叫的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0xFE,
        "哎呀，真的很好吃啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_700E")

    label("loc_6D5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6DBC")

    ChrTalk(    #490
        0xFE,
        (
            "在我晕过去之前，\x01",
            "好像听到了钟声……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xFE,
        (
            "因为记忆有点模糊了，\x01",
            "我也不敢确定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E30")

    label("loc_6DBC")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #492
        0xFE,
        "大桥上的钟声吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "这么一说，我在\x01",
            "被袭击之前似乎听到过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "嗯～抱歉。\x01",
            "记忆实在是不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E30")

    Jump("loc_700E")

    label("loc_6E33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6E95")

    ChrTalk(    #495
        0xFE,
        (
            "我当时在事务所，\x01",
            "如果有人来收拾的话\x01",
            "我应该会注意到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0xFE,
        "嗯～真奇怪啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F4B")

    label("loc_6E95")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #497
        0xFE,
        (
            "咦，说起来\x01",
            "是谁收拾的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        (
            "对、对不起，\x01",
            "我记不得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x101,
        (
            "#1002F不过你人在事务所吧？\x02\x03",

            "如果有人来收拾的话\x01",
            "你应该能注意到的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0xFE,
        (
            "嗯～是啊。\x01",
            "我自己也觉得很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4B")

    Jump("loc_700E")

    label("loc_6F4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_6FBC")

    ChrTalk(    #501
        0xFE,
        (
            "听见钟声时\x01",
            "贝尔夫在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xFE,
        "问我也没用啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0xFE,
        (
            "因为我连有没有听到\x01",
            "过钟声都记不得了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7008")

    label("loc_6FBC")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #504
        0xFE,
        (
            "听见钟声时\x01",
            "贝尔夫在哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0xFE,
        (
            "不，我不知道……\x01",
            "他有嫌疑吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7008")

    Jump("loc_700E")

    label("loc_700B")

    Jump("loc_700E")

    label("loc_700E")

    Return()

    # Function_13_6A4D end

    def Function_14_700F(): pass

    label("Function_14_700F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7345")
    EventBegin(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8B(0x101, 0x164E, 0x1E, 0x190)

    ChrTalk(    #506
        0x101,
        "#1011F啊……！？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(2870, 0, 2140, 0)
    SetChrPos(0x101, 560, 0, 2430, 122)
    SetChrPos(0x105, -370, 0, 2740, 122)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_70B2")
    OP_4A(0x15, 0)
    OP_43(0x15, 0x1, 0x1, 0x1B)
    Jump("loc_70C4")

    label("loc_70B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_70C4")
    OP_4A(0x16, 0)
    OP_43(0x16, 0x1, 0x1, 0x1B)

    label("loc_70C4")

    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_70F5")

    def lambda_70D6():

        label("loc_70D6")

        TurnDirection(0x101, 0x15, 400)
        OP_48()
        Jump("loc_70D6")

    QueueWorkItem2(0x101, 2, lambda_70D6)

    def lambda_70E7():

        label("loc_70E7")

        TurnDirection(0x105, 0x15, 400)
        OP_48()
        Jump("loc_70E7")

    QueueWorkItem2(0x105, 2, lambda_70E7)
    Jump("loc_711E")

    label("loc_70F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_711E")

    def lambda_7102():

        label("loc_7102")

        TurnDirection(0x101, 0x16, 400)
        OP_48()
        Jump("loc_7102")

    QueueWorkItem2(0x101, 2, lambda_7102)

    def lambda_7113():

        label("loc_7113")

        TurnDirection(0x105, 0x16, 400)
        OP_48()
        Jump("loc_7113")

    QueueWorkItem2(0x105, 2, lambda_7113)

    label("loc_711E")

    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_712F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_712F)
    OP_4A(0x17, 0)
    OP_43(0x17, 0x1, 0x1, 0x1C)

    def lambda_714C():
        OP_6D(560, 0, 2430, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_714C)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #507
        0x101,
        (
            "#1000F事务所的\x01",
            "询问已经结束了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_71C4")

    ChrTalk(    #508
        0x15,
        (
            "#050F嗯，完成了。\x02\x03",

            "……你们那边怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71F8")

    label("loc_71C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_71F8")

    ChrTalk(    #509
        0x16,
        (
            "#020F嗯，已经完成了。\x02\x03",

            "你们那边怎么样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71F8")


    ChrTalk(    #510
        0x101,
        (
            "#1015F嗯，也差不多了。\x02\x03",

            "#1006F好，再仔细调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7255")

    ChrTalk(    #511
        0x15,
        "#050F……别松懈啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7277")

    label("loc_7255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7277")

    ChrTalk(    #512
        0x16,
        "#020F调查不能松懈哦。\x02",
    )

    CloseMessageWindow()

    label("loc_7277")


    ChrTalk(    #513
        0x101,
        "#1000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_72A4")
    OP_43(0x15, 0x1, 0x1, 0x1D)
    Jump("loc_72B2")

    label("loc_72A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_72B2")
    OP_43(0x16, 0x1, 0x1, 0x1D)

    label("loc_72B2")

    Sleep(400)
    OP_43(0x17, 0x1, 0x1, 0x1E)
    WaitChrThread(0x17, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_72E2")
    SetChrPos(0x15, -3320, 0, 9510, 45)
    OP_4B(0x15, 0)
    Jump("loc_72FE")

    label("loc_72E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_72FE")
    SetChrPos(0x16, -3320, 0, 9510, 45)
    OP_4B(0x16, 0)

    label("loc_72FE")

    SetChrPos(0x17, -2620, 0, 8220, 0)
    OP_4B(0x17, 0)
    OP_28(0x6A, 0x1, 0x10)
    SetChrPos(0x14, -7880, 0, 83450, 0)
    SetChrPos(0xE, -3740, 0, 78670, 0)
    OP_44(0x101, 0x2)
    OP_44(0x105, 0x2)
    EventEnd(0x0)

    label("loc_7345")

    Return()

    # Function_14_700F end

    def Function_15_7346(): pass

    label("Function_15_7346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7438")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7392")

    ChrTalk(    #514
        0x101,
        "#1007F还不能出去啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_73C3")

    label("loc_7392")

    OP_A2(0x9)

    ChrTalk(    #515
        0x101,
        (
            "#1015F啊，这边是门口了。\x02\x03",

            "得先回去询问。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73C3")

    Jump("loc_741D")

    label("loc_73C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_73EF")

    ChrTalk(    #516
        0x105,
        "#042F还不能去别的地方啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_741D")

    label("loc_73EF")

    OP_A2(0x9)

    ChrTalk(    #517
        0x105,
        (
            "#042F这边是门口呢。\x02\x03",

            "得先回去询问呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741D")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7438")

    Return()

    # Function_15_7346 end

    def Function_16_7439(): pass

    label("Function_16_7439")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xFE, 0x0, 0)
    OP_4A(0xFE, 0)
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0x1, 0xFE, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【说话】\x01",      # 0
            "【报告】\x01",      # 1
            "【放弃】\x01",      # 2
            "【取消】\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_74CC"),
        (1, "loc_750B"),
        (2, "loc_7535"),
        (SWITCH_DEFAULT, "loc_7756"),
    )


    label("loc_74CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_74DA")
    Call(1, 17)
    Jump("loc_74E5")

    label("loc_74DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_74E5")
    Call(1, 18)

    label("loc_74E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_74FA")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_7501")

    label("loc_74FA")

    OP_8C(0xFE, 0, 0)

    label("loc_7501")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_777C")

    label("loc_750B")

    Call(1, 19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7524")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_752B")

    label("loc_7524")

    OP_8C(0xFE, 0, 0)

    label("loc_752B")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_777C")

    label("loc_7535")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #518
        "\x07\x05要放弃吗？\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【放弃】\x01",            # 0
            "【再努力一下】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_75D7")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_75DE")

    label("loc_75D7")

    OP_8C(0xFE, 0, 0)

    label("loc_75DE")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    label("loc_75E6")

    EventBegin(0x0)
    TurnDirection(0x17, 0x0, 0)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7665")

    ChrTalk(    #519
        0x15,
        (
            "#052F……要放弃查吗？\x02\x03",

            "#053F算了，随便你了。\x02\x03",

            "#050F我会继续调查的。\x01",
            "在我搞定之前你就在外面等着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E3")

    label("loc_7665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_76E3")

    ChrTalk(    #520
        0x16,
        (
            "#023F……要放弃调查吗？\x02\x03",

            "#026F算了，如果没自信\x01",
            "解决的话也没办法。\x02\x03",

            "#022F我会继续调查的。\x01",
            "你就在外边先等候一会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E3")

    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #521
        "\x07\x02任务【选举事务所的伤人事件】\x07\x00失败了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x69, 0x4, 0x80)
    OP_28(0x69, 0x4, 0x40)
    OP_28(0x69, 0x1, 0x4000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_777C")

    label("loc_7756")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_776B")
    TurnDirection(0xFE, 0xA, 0)
    Jump("loc_7772")

    label("loc_776B")

    OP_8C(0xFE, 0, 0)

    label("loc_7772")

    OP_4B(0xFE, 0)
    TalkEnd(0xFE)
    Jump("loc_777C")

    label("loc_777C")

    Return()

    # Function_16_7439 end

    def Function_17_777D(): pass

    label("Function_17_777D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_77C6")

    ChrTalk(    #522
        0xFE,
        (
            "#050F看来快要找到事件的真相了。\x02\x03",

            "有了眉目就来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B59")

    label("loc_77C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_7847")

    ChrTalk(    #523
        0xFE,
        (
            "#050F到了现在\x01",
            "又有重要的证词出现了。\x02\x03",

            "如果没头绪的话就把\x01",
            "询问过的内容再询问一遍看看。\x02\x03",

            "放弃的话就前功尽弃了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B59")

    label("loc_7847")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_789C")

    ChrTalk(    #524
        0xFE,
        (
            "#050F钟声吗……\x01",
            "确实是一个线索。\x02\x03",

            "没关系。\x01",
            "就按你所想的去尝试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B59")

    label("loc_789C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7935")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7902")

    ChrTalk(    #525
        0xFE,
        (
            "#050F艾丝蒂尔你们\x01",
            "去查一下刚才的证词内容吧。\x02\x03",

            "我们再稍微\x01",
            "在这里停留一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7932")

    label("loc_7902")


    ChrTalk(    #526
        0xFE,
        (
            "#050F有什么发现吗？\x02\x03",

            "别放弃，要坚持\x01",
            "追查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7932")

    Jump("loc_7B59")

    label("loc_7935")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_79DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_79A1")

    ChrTalk(    #527
        0xFE,
        (
            "#050F艾丝蒂尔你们去\x01",
            "去查一下刚才的证词内容吧。\x02\x03",

            "我们再稍微\x01",
            "在这里停留一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79DB")

    label("loc_79A1")


    ChrTalk(    #528
        0xFE,
        (
            "#050F有新线索了呢。\x02\x03",

            "希望能在其中\x01",
            "找到可信的证词……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DB")

    Jump("loc_7B59")

    label("loc_79DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_7A26")

    ChrTalk(    #529
        0xFE,
        (
            "#050F嫌疑人仍然很模糊。\x02\x03",

            "该是扩大调查\x01",
            "范围的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B59")

    label("loc_7A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7A93")

    ChrTalk(    #530
        0xFE,
        (
            "#050F嫌疑人都已经询问过了，\x01",
            "不过他们说的话都含糊不清。\x02\x03",

            "别被那些刻意编排的\x01",
            "证词给蒙蔽了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B59")

    label("loc_7A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7B13")
    Jc((scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7AD3")

    ChrTalk(    #531
        0xFE,
        "#050F……明白的话就快点开工吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B10")

    label("loc_7AD3")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #532
        0xFE,
        (
            "#050F有什么新的线索了吗？\x02\x03",

            "有的话就追查下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B10")

    Jump("loc_7B59")

    label("loc_7B13")


    ChrTalk(    #533
        0xFE,
        (
            "#050F先去询问有关嫌疑人的问题。\x02\x03",

            "如果有新的线索\x01",
            "就继续追查下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B59")

    Return()

    # Function_17_777D end

    def Function_18_7B5A(): pass

    label("Function_18_7B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_7BA8")

    ChrTalk(    #534
        0xFE,
        (
            "#020F快要看到结果了呢。\x02\x03",

            "确定了嫌疑人的话\x01",
            "就马上来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7E")

    label("loc_7BA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_7C31")

    ChrTalk(    #535
        0xFE,
        (
            "#022F到了现在\x01",
            "又有重要的证词出现了呢。\x02\x03",

            "如果没头绪的话就把以前\x01",
            "询问过的内容再询问一遍看看。\x02\x03",

            "放弃的话就前功尽弃了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7E")

    label("loc_7C31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_7C7B")

    ChrTalk(    #536
        0xFE,
        (
            "#020F原来如此，钟声啊……\x02\x03",

            "想法不错。\x01",
            "按你的想法做吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7E")

    label("loc_7C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7D3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7CE5")

    ChrTalk(    #537
        0xFE,
        (
            "#022F艾丝蒂尔你们\x01",
            "去追查一下刚才的证词的内容吧。\x02\x03",

            "我们再稍微\x01",
            "在这里停留一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D3B")

    label("loc_7CE5")


    ChrTalk(    #538
        0xFE,
        (
            "#020F咦，有什么发现吗？\x02\x03",

            "询问情况最需要坚韧不拔的毅力。\x01",
            "不要放弃，继续追查下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D3B")

    Jump("loc_7F7E")

    label("loc_7D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7DE9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7DAC")

    ChrTalk(    #539
        0xFE,
        (
            "#022F艾丝蒂尔你们\x01",
            "去追查一下刚才的证词的内容吧。\x02\x03",

            "我们再稍微\x01",
            "在这里停留一会儿。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DE6")

    label("loc_7DAC")


    ChrTalk(    #540
        0xFE,
        (
            "#020F有新线索了呢。\x02\x03",

            "希望能在其中\x01",
            "找到可信的证词……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DE6")

    Jump("loc_7F7E")

    label("loc_7DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_7E35")

    ChrTalk(    #541
        0xFE,
        (
            "#020F嫌疑人仍然很模糊啊。\x02\x03",

            "该是扩大调查\x01",
            "范围的时候了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7E")

    label("loc_7E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7EA0")

    ChrTalk(    #542
        0xFE,
        (
            "#020F嫌疑人都已经询问过了，\x01",
            "不过他们说的话都含糊不清。\x02\x03",

            "要相信哪个证词\x01",
            "需要慎重地思考。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F7E")

    label("loc_7EA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7F2D")
    Jc((scpexpr(EXPR_GET_RESULT, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7EEA")

    ChrTalk(    #543
        0xFE,
        (
            "#020F喂喂，还在磨蹭什么。\x02\x03",

            "快点回去调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F2A")

    label("loc_7EEA")

    RunExpression(0xB, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #544
        0xFE,
        (
            "#020F发现什么线索了吗？\x02\x03",

            "如果有的话\x01",
            "就追查下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2A")

    Jump("loc_7F7E")

    label("loc_7F2D")


    ChrTalk(    #545
        0xFE,
        (
            "#020F首先要从收集\x01",
            "嫌疑人的情报开始。\x02\x03",

            "如果发现什么线索的话\x01",
            "就立即追查下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F7E")

    Return()

    # Function_18_7B5A end

    def Function_19_7F7F(): pass

    label("Function_19_7F7F")

    EventBegin(0x0)
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x17, 0x101, 0)
    OP_4A(0x17, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7FD9")
    TurnDirection(0x15, 0x101, 0)

    ChrTalk(    #546
        0x15,
        (
            "#052F……有眉目了吗？\x02\x03",

            "#057F那么嫌疑犯是谁？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_801D")

    label("loc_7FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_801D")
    TurnDirection(0x16, 0x101, 0)

    ChrTalk(    #547
        0x16,
        (
            "#023F……知道犯人是谁了？\x02\x03",

            "#022F那么谁是嫌疑犯？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801D")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #548
        "\x18伤害案的犯人是谁？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "昆茨")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_80D4")
    OP_CC(0x1, 0x0, "诺曼")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_810B")
    OP_CC(0x1, 0x0, "海利欧")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_810B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_8144")
    OP_CC(0x1, 0x0, "亚内斯特")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8144")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_817F")
    OP_CC(0x1, 0x0, "穆拉德老人")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_817F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_81B6")
    OP_CC(0x1, 0x0, "贝尔夫")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81B6")

    OP_CC(0x1, 0x0, "离开")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_830D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82AB")

    ChrTalk(    #549
        0x15,
        (
            "#055F啊……！？\x02\x03",

            "你说这个大叔\x01",
            "是犯人吗？\x02\x03",

            "#551F算了……\x01",
            "先说说排除第一个\x01",
            "嫌疑人的理由吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_830A")

    label("loc_82AB")


    ChrTalk(    #550
        0x15,
        (
            "#055F啊……！？\x02\x03",

            "你说那个大叔\x01",
            "是犯人吗？\x02\x03",

            "#551F算了……\x01",
            "先说说排除第一个\x01",
            "嫌疑人的理由吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_830A")

    Jump("loc_83FC")

    label("loc_830D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_83FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8399")

    ChrTalk(    #551
        0x16,
        (
            "#023F啊……！？\x01",
            "你说这个人是犯人？\x02\x03",

            "#025F有确凿的\x01",
            "根据吗？\x02\x03",

            "先说说排除第一个\x01",
            "嫌疑人的理由吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83FC")

    label("loc_8399")


    ChrTalk(    #552
        0x16,
        (
            "#023F啊……！？\x01",
            "你说那个人是犯人？\x02\x03",

            "#025F有确凿的\x01",
            "根据吗？\x02\x03",

            "先说说排除第一个\x01",
            "嫌疑人的理由吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83FC")

    OP_A3(0xC)
    Call(1, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_84BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8464")

    ChrTalk(    #553
        0x15,
        (
            "#050F那么，接下来就要拿出\x01",
            "这个嫌疑人犯罪的证明了……\x02\x03",

            "……你有什么根据吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84BB")

    label("loc_8464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_84BB")

    ChrTalk(    #554
        0x16,
        (
            "#027F那么，接下来就要拿出\x01",
            "这个嫌疑人犯罪的证明了……\x02\x03",

            "……你有什么根据吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84BB")

    Call(1, 21)

    label("loc_84BF")

    Jump("loc_88F0")

    label("loc_84C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8512")

    ChrTalk(    #555
        0x15,
        (
            "#057F……最初的嫌疑人吗。\x02\x03",

            "那根据是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8548")

    label("loc_8512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8548")

    ChrTalk(    #556
        0x16,
        (
            "#022F……最初的嫌疑人啊。\x02\x03",

            "那根据是什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8548")

    Call(1, 22)
    Jump("loc_88F0")

    label("loc_854F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_85B4")

    ChrTalk(    #557
        0x15,
        (
            "#052F……哟，是第一发现人吗？\x02\x03",

            "#050F那么你这么想的根据是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85FA")

    label("loc_85B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_85FA")

    ChrTalk(    #558
        0x16,
        (
            "#023F……哟，那不是第一发现人吗？\x02\x03",

            "你这么想的根据是什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85FA")

    OP_A3(0xD)
    Call(1, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_86D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_866B")

    ChrTalk(    #559
        0x15,
        (
            "#050F但如果是这样的话，\x01",
            "最初的嫌疑人又是怎么回事呢？\x02\x03",

            "有可以否定\x01",
            "昆茨犯罪的根据吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86C9")

    label("loc_866B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_86C9")

    ChrTalk(    #560
        0x16,
        (
            "#022F如果是这样的话，\x01",
            "最初的嫌疑人又是怎么回事呢？\x02\x03",

            "有可以否定\x01",
            "昆茨犯罪的根据吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86C9")

    OP_A2(0x10)
    Call(1, 20)

    label("loc_86D0")

    Jump("loc_88F0")

    label("loc_86D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_874F")

    ChrTalk(    #561
        0x15,
        (
            "#050F……渡鸦帮的小子啊。\x02\x03",

            "你有确凿的\x01",
            "根据吧？\x02\x03",

            "先说说排除第一个\x01",
            "嫌疑人昆茨的理由吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87B3")

    label("loc_874F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_87B3")

    ChrTalk(    #562
        0x16,
        (
            "#022F……渡鸦帮的小子啊。\x02\x03",

            "你有确凿的\x01",
            "根据吗？\x02\x03",

            "说说排除第一个\x01",
            "嫌疑人昆茨先生的理由吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B3")

    OP_A3(0xC)
    Call(1, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_887E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_881F")

    ChrTalk(    #563
        0x15,
        (
            "#050F那么接下来就要拿出\x01",
            "这个嫌疑人犯罪的证明了……\x02\x03",

            "……那你有什么样的根据呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_887A")

    label("loc_881F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_887A")

    ChrTalk(    #564
        0x16,
        (
            "#022F那么接下来就要拿出\x01",
            "这个嫌疑人犯罪的证明了……\x02\x03",

            "……那你有什么样的根据呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_887A")

    Call(1, 24)

    label("loc_887E")

    Jump("loc_88F0")

    label("loc_8881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_88BC")

    ChrTalk(    #565
        0x15,
        (
            "#050F什么啊，还没确定？\x02\x03",

            "好了，仔细调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88F0")

    label("loc_88BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_88F0")

    ChrTalk(    #566
        0x16,
        (
            "#020F咦，还没确定？\x02\x03",

            "好了，仔细调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88F0")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x17, 255)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    # Function_19_7F7F end

    def Function_20_8906(): pass

    label("Function_20_8906")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #567
        "\x18否定昆茨犯罪的根据呢？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：没什么根据，只不过那么想而已】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_8A0F")
    OP_CC(0x1, 0x0, "【他本人的证词：　发出声响的时候在户外】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_8A70")
    OP_CC(0x1, 0x0, "【已被证明的事实：预想的犯罪时间内有不在场证明】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A70")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #568
        (
            "\x07\x05你说的犯罪理由\x01",
            "好歹能够成立。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8B3C")

    ChrTalk(    #569
        0x15,
        (
            "#053F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7A")

    label("loc_8B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8B7A")

    ChrTalk(    #570
        0x16,
        (
            "#025F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B7A")


    ChrTalk(    #571
        0x101,
        "#1007F明、明白了……\x02",
    )

    CloseMessageWindow()
    OP_A3(0xC)
    Jump("loc_9076")

    label("loc_8B9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CFE")

    ChrTalk(    #572
        0x101,
        (
            "#1002F那个巨大的响声发出时，\x01",
            "据他本人说他在户外。\x02\x03",

            "如果那个是犯罪发生时的声音的话，\x01",
            "那么昆茨先生就不是嫌疑人了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8C86")

    ChrTalk(    #573
        0x15,
        (
            "#551F这只是他本人的辩解吧？\x02\x03",

            "#057F怎么能随便地相信这些？\x01",
            "取得证明之后再来说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CDE")

    label("loc_8C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8CDE")

    ChrTalk(    #574
        0x16,
        (
            "#025F这只是他本人的辩解吧？\x02\x03",

            "#022F怎么能随便地相信这些？\x01",
            "证实之后再来说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CDE")


    ChrTalk(    #575
        0x101,
        "#1007F明、明白了……\x02",
    )

    CloseMessageWindow()
    OP_A3(0xC)
    Jump("loc_9076")

    label("loc_8CFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9076")

    ChrTalk(    #576
        0x101,
        (
            "#1002F那个巨大的响声发出时，\x01",
            "昆茨先生确实在外面哦。\x02\x03",

            "从诺曼先生的证词中\x01",
            "可以确认这一点。\x02\x03",

            "如果那个是犯罪发生时的声音的话，\x01",
            "昆茨先生是犯人的可能性就很低了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8E04")

    ChrTalk(    #577
        0x15,
        (
            "#053F哟，原来是这样……\x02\x03",

            "那么同时海利欧的\x01",
            "嫌疑也可以拿掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E59")

    label("loc_8E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8E59")

    ChrTalk(    #578
        0x16,
        (
            "#022F原来如此，很合理的分析。\x02\x03",

            "那么同时海利欧先生的\x01",
            "嫌疑也可以拿掉了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_9038")
    OP_A3(0x10)

    ChrTalk(    #579
        0x101,
        (
            "#1002F嗯，是啊。\x02\x03",

            "海利欧先生也确实\x01",
            "和诺曼先生会合了……\x02\x03",

            "#1015F……等等，咦、咦咦！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8F04")

    ChrTalk(    #580
        0x15,
        (
            "#057F喂，你点什么头啊？\x02\x03",

            "你刚才还在说\x01",
            "海利欧是犯人的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F4F")

    label("loc_8F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8F4F")

    ChrTalk(    #581
        0x16,
        (
            "#025F唉，你同意个什么啊……\x02\x03",

            "你刚才还在说\x01",
            "海利欧先生是犯人的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F4F")


    ChrTalk(    #582
        0x101,
        (
            "#1008F啊，哈哈……抱歉。\x02\x03",

            "头脑混乱到自己都不知道\x01",
            "自己在说些什么了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8FDE")

    ChrTalk(    #583
        0x15,
        (
            "#053F把你要说的话整理好\x01",
            "再来吧。\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_901B")

    label("loc_8FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_901B")

    ChrTalk(    #584
        0x16,
        (
            "#026F整理一下论点\x01",
            "再来吧。\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_901B")


    ChrTalk(    #585
        0x101,
        "#1007F明、明白了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9076")

    label("loc_9038")


    ChrTalk(    #586
        0x101,
        (
            "#1015F嗯，是啊。\x02\x03",

            "海利欧先生也确实\x01",
            "和诺曼先生会合了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_9076")

    Return()

    # Function_20_8906 end

    def Function_21_9077(): pass

    label("Function_21_9077")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #587
        "\x18证明嫌疑人犯罪的根据是？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：没什么根据，只不过那么想而已】")
    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #588
        (
            "\x07\x05你说的犯罪理由\x01",
            "好歹能够成立。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_91A8")

    ChrTalk(    #589
        0x15,
        (
            "#053F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91E6")

    label("loc_91A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_91E6")

    ChrTalk(    #590
        0x16,
        (
            "#025F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91E6")


    ChrTalk(    #591
        0x101,
        "#1007F明、明白了……\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_21_9077 end

    def Function_22_9201(): pass

    label("Function_22_9201")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #592
        "\x18证明昆茨犯罪的根据是？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：从状况判断应该那样考虑】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_9306")
    OP_CC(0x1, 0x0, "【有关人员的证词：案件发生时嫌疑人在生气】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_9367")
    OP_CC(0x1, 0x0, "【已被证明的事实：预想的犯罪时间内有不在场证明】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9367")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93FA")

    ChrTalk(    #593
        0x101,
        (
            "#1002F案件发生时的状况是最大的根据。\x02\x03",

            "想想桥上的骚乱，\x01",
            "就能发现他的动机充足。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_957E")

    label("loc_93FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94AA")

    ChrTalk(    #594
        0x101,
        (
            "#1002F首先状况是最大的根据。\x02\x03",

            "而且可以说动机也很充分。\x02\x03",

            "桥上的骚乱是最近的事，\x01",
            "气没消也是很正常的。\x02\x03",

            "因为确实有相关人员作证\x01",
            "说嫌疑人当时在生气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_957E")

    label("loc_94AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_957E")

    ChrTalk(    #595
        0x101,
        (
            "#1002F那个巨大的响声发出时，\x01",
            "昆茨先生确实在外面哦。\x02\x03",

            "从诺曼先生的证词中\x01",
            "可以确认这一点。\x02\x03",

            "如果那个是犯罪发生时的声音的话，\x01",
            "嫌疑人是犯人的可能性就很低了……\x02\x03",

            "#1015F……等等，咦、咦咦？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_957E")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_95E5")

    ChrTalk(    #596
        0x15,
        (
            "#053F喂，你到底想说些什么？\x02\x03",

            "这样一来昆茨\x01",
            "不就不可能是犯人了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_962E")

    label("loc_95E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_962E")

    ChrTalk(    #597
        0x16,
        (
            "#025F你到底想说些什么？\x02\x03",

            "这样一来昆茨\x01",
            "不就不可能是犯人了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_962E")


    ChrTalk(    #598
        0x101,
        (
            "#1008F啊，哈哈……抱歉。\x02\x03",

            "头脑混乱到自己都不知道\x01",
            "自己在说些什么了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_96BD")

    ChrTalk(    #599
        0x15,
        (
            "#053F把你要说的话整理好\x01",
            "再来吧。\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96FA")

    label("loc_96BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_96FA")

    ChrTalk(    #600
        0x16,
        (
            "#026F整理一下论点\x01",
            "再来吧。\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96FA")

    Jump("loc_98D3")

    label("loc_96FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_97A3")

    ChrTalk(    #601
        0x15,
        (
            "#053F嗯，确实是这样……\x02\x03",

            "#050F可凭你刚才举出的这些根据，\x01",
            "还不能否定所有其它的可能性。\x02\x03",

            "就是说在这家伙之前可能\x01",
            "已经有人进入房间了。\x02\x03",

            "你敢说这不可能吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9846")

    label("loc_97A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9846")

    ChrTalk(    #602
        0x16,
        (
            "#026F嗯，你所说的不错……\x02\x03",

            "#022F可凭你刚才举出的这些根据，\x01",
            "还不能否定所有其它的可能性。\x02\x03",

            "就是说在这那之前可能\x01",
            "已经有人进入房间了。\x02\x03",

            "你敢说这不可能吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9846")


    ChrTalk(    #603
        0x101,
        "#1015F这、这个……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_989B")

    ChrTalk(    #604
        0x15,
        (
            "#053F那就再继续调查吧。\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D3")

    label("loc_989B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_98D3")

    ChrTalk(    #605
        0x16,
        (
            "#027F那就再继续调查吧\x02\x03",

            "……然后我们再讨论。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D3")


    ChrTalk(    #606
        0x101,
        "#1007F明、明白了……\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_22_9201 end

    def Function_23_98EE(): pass

    label("Function_23_98EE")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #607
        "\x18证明海利欧是犯人的根据呢？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：没什么根据，只不过那么想而已】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_99F9")
    OP_CC(0x1, 0x0, "【有关人员的证词：午饭后去过犯罪现场】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_9A50")
    OP_CC(0x1, 0x0, "【已被证明的事实：午饭后去过犯罪现场】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A50")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7A")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #608
        (
            "\x07\x05你说的犯罪理由\x01",
            "好歹能够成立。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9B1C")

    ChrTalk(    #609
        0x15,
        (
            "#053F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B5A")

    label("loc_9B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9B5A")

    ChrTalk(    #610
        0x16,
        (
            "#025F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B5A")


    ChrTalk(    #611
        0x101,
        "#1007F明，明白了……\x02",
    )

    CloseMessageWindow()
    OP_A3(0xD)
    Jump("loc_9CB2")

    label("loc_9B7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF8")

    ChrTalk(    #612
        0x101,
        (
            "#1002F有人目击海利欧先生\x01",
            "在案件发生之前不久上了２楼。\x02\x03",

            "而且，他本人并没有\x01",
            "积极地提供这一内容。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CB2")

    label("loc_9BF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CB2")

    ChrTalk(    #613
        0x101,
        (
            "#1010F案件发生之前不久海利欧先生\x01",
            "在事务所这点已经确定。\x02\x03",

            "而且，他本人并没有\x01",
            "积极地提供这一内容……\x02\x03",

            "#1002F隐瞒曾在犯罪现场这一点\x01",
            "就等于是在承认自己就是犯人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CCC")
    Jump("loc_9DCC")

    label("loc_9CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9D15")

    ChrTalk(    #614
        0x15,
        (
            "#050F就是说有了可以怀疑他的证据是吧？\x02\x03",

            "……动机怎么说呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5B")

    label("loc_9D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9D5B")

    ChrTalk(    #615
        0x16,
        (
            "#020F就是说有了可以怀疑他的证据是吧？\x02\x03",

            "……动机怎么说呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D5B")


    ChrTalk(    #616
        0x101,
        (
            "#1015F他和受害者是竞争\x01",
            "二号人物的对手关系。\x02\x03",

            "虽然作为动机有点不够充分，\x01",
            "不过在现在这种情况下就不好说了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_9DCC")

    Return()

    # Function_23_98EE end

    def Function_24_9DCD(): pass

    label("Function_24_9DCD")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #617
        "\x18能证明贝尔夫犯罪的根据呢？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：没什么根据，只不过那么想而已】")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_9E8C")
    OP_CC(0x1, 0x0, "【已被证明的事实：预想的犯罪时间内没有不在场证明】")

    label("loc_9E8C")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FAA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #618
        (
            "\x07\x05你说的犯罪理由\x01",
            "好歹能够成立。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9F4E")

    ChrTalk(    #619
        0x15,
        (
            "#053F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F8C")

    label("loc_9F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_9F8C")

    ChrTalk(    #620
        0x16,
        (
            "#025F不行，这根本不象话……\x02\x03",

            "好好地再去调查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F8C")


    ChrTalk(    #621
        0x101,
        "#1007F明，明白了……\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_9FAA")


    ChrTalk(    #622
        0x101,
        (
            "#1002F根据就是他的不在现场证明。\x02\x03",

            "有力的证词和他本人提供的\x01",
            "不在现场证明相抵触。\x02\x03",

            "#1015F因为昆茨先生和海利欧先生\x01",
            "是犯人的可能性已经被否定了……\x02\x03",

            "这个人是最后一个\x01",
            "有可能是犯人的人。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A0DE")

    ChrTalk(    #623
        0x15,
        (
            "#053F嗯，按照排除法的话确实是这样。\x02\x03",

            "#050F……但说到底这\x01",
            "只能构成条件证据。\x02\x03",

            "就没有更具有决定性的证据了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A154")

    label("loc_A0DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A154")

    ChrTalk(    #624
        0x16,
        (
            "#026F嗯，按照排除法的话确实是这样。\x02\x03",

            "#022F……但说到底这\x01",
            "只能构成条件证据。\x02\x03",

            "还需要更具有决定性的证据呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A154")

    FadeToDark(300, 0, 100)
    RunExpression(0xC, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #625
        "\x18支持贝尔夫就是犯人的证据呢？\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    OP_CC(0x1, 0x0, "【游击士的直觉：虽然没什么证据，不过我就是这么认为】")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_A20B")
    OP_CC(0x1, 0x0, "【证词矛盾：他知道特制什锦饭的事】")

    label("loc_A20B")

    OP_CC(0x2, 0x0)
    MenuEnd(0xC)
    OP_5F(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A36F")

    ChrTalk(    #626
        0x101,
        (
            "#1007F嗯、嗯……虽然这么说。\x02\x03",

            "不过没什么特别有力的证据。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2E7")

    ChrTalk(    #627
        0x15,
        (
            "#053F是吗……\x02\x03",

            "#050F那就再好好调查一下吧。\x02\x03",

            "已经到最后关头了。\x01",
            "只差一步应该就能解决案件了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A34F")

    label("loc_A2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A34F")

    ChrTalk(    #628
        0x16,
        (
            "#026F是吗……\x02\x03",

            "#027F那就再好好调查一下吧。\x02\x03",

            "已经到最后关头了。\x01",
            "只差一步应该就能解决案件了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A34F")


    ChrTalk(    #629
        0x101,
        "#1002F嗯，我会努力的。\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_A36F")


    ChrTalk(    #630
        0x101,
        (
            "#1015F虽然不知道是不是决定性的……\x02\x03",

            "不过关于特制什锦饭的证词\x01",
            "应该可以作为案件的参考。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A3ED")

    ChrTalk(    #631
        0x15,
        "#052F哦？怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A40D")

    label("loc_A3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A40D")

    ChrTalk(    #632
        0x16,
        "#023F嗯？怎么回事？\x02",
    )

    CloseMessageWindow()

    label("loc_A40D")


    ChrTalk(    #633
        0x101,
        (
            "#1002F嗯，贝尔夫先生说\x01",
            "他是在１楼吃的午饭……\x02\x03",

            "可为什么他能看见在２楼的\x01",
            "诺曼先生吃的特制什锦饭呢？\x02\x03",

            "而且连诺曼先生没吃完\x01",
            "他都知道啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A4DB")

    ChrTalk(    #634
        0x15,
        (
            "#057F也就是说他上过２楼……\x02\x03",

            "……你想说的是这个吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A51B")

    label("loc_A4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A51B")

    ChrTalk(    #635
        0x16,
        (
            "#022F也就是说他上过２楼……\x02\x03",

            "……你想说的是这个吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A51B")


    ChrTalk(    #636
        0x101,
        "#1002F嗯……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A5B1")

    ChrTalk(    #637
        0x15,
        (
            "#053F……………………\x02\x03",

            "#057F……好，我知道了。\x02\x03",

            "那就叫来贝尔夫\x01",
            "问个清楚吧。\x02\x03",

            "因为凭手头这点证据，\x01",
            "还很难马上逮捕他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A653")

    label("loc_A5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A653")

    ChrTalk(    #638
        0x16,
        (
            "#026F……………………\x02\x03",

            "#022F……明白了。\x01",
            "我也基本上能够接受这一观点。\x02\x03",

            "这样一来只能把他本人\x01",
            "叫来问个清楚了。\x02\x03",

            "因为凭手头这点证据，\x01",
            "还很难马上逮捕他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A653")


    ChrTalk(    #639
        0x101,
        "#1002F嗯、嗯……明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(1, 25)
    Return()

    # Function_24_9DCD end

    def Function_25_A681(): pass

    label("Function_25_A681")

    OP_6D(-44480, 0, 26180, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(72000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF, -46590, 0, 26370, 105)
    SetChrPos(0x101, -44610, 0, 25830, 300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A6FF")
    SetChrPos(0x15, -44620, 0, 24750, 300)
    OP_4A(0x15, 0)
    Jump("loc_A71B")

    label("loc_A6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A71B")
    SetChrPos(0x16, -44620, 0, 24750, 300)
    OP_4A(0x16, 0)

    label("loc_A71B")

    OP_4A(0xF, 255)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #640
        0xF,
        (
            "怎、怎么了！？\x01",
            "把我叫到这里来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #641
        0xF,
        "我、我可什么都没做啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #642
        0x101,
        (
            "#1016F好了，冷静一点。\x02\x03",

            "我们又不会把你\x01",
            "给吃了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A7EA")

    ChrTalk(    #643
        0x15,
        (
            "#050F#2P如果你配合我们调查的话\x01",
            "很快就能回去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A826")

    label("loc_A7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A826")

    ChrTalk(    #644
        0x16,
        (
            "#020F#2P如果你配合我们调查的话\x01",
            "很快就能回去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A826")


    ChrTalk(    #645
        0xF,
        "配、配合……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #646
        0x101,
        (
            "#1002F嗯，希望你老实回答。\x02\x03",

            "……你午饭之后去了哪里？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #647
        0xF,
        "我、我说了我一直在地下……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A8F4")

    ChrTalk(    #648
        0x15,
        (
            "#057F#2P我可有言在先……\x02\x03",

            "你撒谎的话是\x01",
            "不可能离开这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A93C")

    label("loc_A8F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A93C")

    ChrTalk(    #649
        0x16,
        (
            "#026F#2P我想提醒你一点……\x02\x03",

            "你撒谎的话是\x01",
            "不可能离开这里的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A93C")

    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #650
        0xF,
        "……唔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #651
        0x101,
        (
            "#1002F你并没有一直\x01",
            "待在地下。\x02\x03",

            "这一点我们已经知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #652
        0xF,
        "……………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AA1E")

    ChrTalk(    #653
        0x15,
        (
            "#050F#2P如果没做什么亏心事的话\x01",
            "就说实话吧。\x02\x03",

            "#053F还是……\x01",
            "已经没那种勇气了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA75")

    label("loc_AA1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AA75")

    ChrTalk(    #654
        0x16,
        (
            "#022F#2P如果没做什么亏心事的话\x01",
            "就说实话吧。\x02\x03",

            "还是……\x01",
            "已经没那种勇气了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA75")


    ChrTalk(    #655
        0xF,
        "……唔……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #656
        0xF,
        "明、明白了……我说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #657
        0xF,
        (
            "今天……\x01",
            "午饭之后……………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #658
        0xF,
        (
            "我……\x01",
            "其实是去了事务所的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #659
        0xF,
        "是去做善后工作的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0x101,
        (
            "#1002F善后工作……？\x02\x03",

            "那么，把餐具返还到\x01",
            "前台的人就是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #661
        0xF,
        "嗯，是我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #662
        0xF,
        (
            "因为大家都很忙，\x01",
            "所以我就想去收拾餐具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #663
        0xF,
        (
            "收拾完我又连\x01",
            "事务所也清扫了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #664
        0xF,
        (
            "呼，想不到这件事会\x01",
            "变成这样……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #665
        0x101,
        (
            "#1004F哎……？\x02\x03",

            "话、话好像有点\x01",
            "接不上……\x02\x03",

            "#1002F你只是收拾了餐具\x01",
            "并且做了扫除吧？\x02\x03",

            "那个怎么会\x01",
            "和案子扯上关系呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AC80")

    ChrTalk(    #666
        0x15,
        "#050F#2P……你知道的吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACA5")

    label("loc_AC80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_ACA5")

    ChrTalk(    #667
        0x16,
        "#027F#2P……你知道的吧。\x02",
    )

    CloseMessageWindow()

    label("loc_ACA5")


    ChrTalk(    #668
        0xF,
        "嗯、嗯………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #669
        0xF,
        "其实……………\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 0)
    OP_4A(0x14, 0)
    OP_4A(0xE, 0)
    OP_4A(0x17, 0)
    SetChrPos(0xB, -3200, 0, 81000, 180)
    SetChrPos(0x14, -2140, 0, 81000, 180)
    SetChrPos(0xE, -1300, 0, 80130, 215)
    SetChrPos(0xF, -2710, 0, 79250, 0)
    SetChrPos(0x101, -3400, 0, 77780, 0)
    SetChrPos(0x17, -3150, 0, 76370, 0)
    SetChrPos(0x105, -2150, 0, 76170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_ADB5")
    SetChrPos(0x15, -2400, 0, 77580, 0)
    Jump("loc_ADCD")

    label("loc_ADB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_ADCD")
    SetChrPos(0x16, -2400, 0, 77580, 0)

    label("loc_ADCD")

    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #670
        0xB,
        "…………呼，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #671
        0xB,
        (
            "我知道贝尔夫为了\x01",
            "清扫而来过这个房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #672
        0xB,
        "这一点和本案……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #673
        0xB,
        (
            "也就是对德尔斯的伤害案\x01",
            "到底有怎样的关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #674
        0x101,
        (
            "#1007F#3P有很大的关系啊。\x02\x03",

            "#1000F总之先听听\x01",
            "他本人的说明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AEEC")

    ChrTalk(    #675
        0x15,
        "#050F……喂，说来听听。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #676
        0xF,
        "啊、啊啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF24")

    label("loc_AEEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AF24")

    ChrTalk(    #677
        0x16,
        "#020F……喂，说明一下吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #678
        0xF,
        "啊、啊啊……\x02",
    )

    CloseMessageWindow()

    label("loc_AF24")


    ChrTalk(    #679
        0xF,
        (
            "房间的扫除结束之后，\x01",
            "正想要回去的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #680
        0xF,
        (
            "因为整理了很多地方，\x01",
            "所以房间蒙上了一层灰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #681
        0xF,
        (
            "然后就打开阳台的门\x01",
            "想让空气流通一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #682
        0xF,
        (
            "不过因为手上的餐具\x01",
            "堆得像山一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0xF,
        "没、没办法的我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #684
        0xF,
        "就、就用力踢开了门。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(30)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)
    OP_43(0x14, 0x1, 0x1, 0x1A)
    Sleep(30)
    OP_43(0xE, 0x1, 0x1, 0x1A)
    OP_43(0xB, 0x1, 0x1, 0x1A)

    def lambda_B092():
        OP_6D(-1140, 0, 84170, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B092)

    def lambda_B0AA():
        OP_6B(3030, 2000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B0AA)
    OP_67(0, 5480, -10000, 2000)

    ChrTalk(    #685
        0x1A,
        "想、想不到那里的门………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #686
        0x101,
        (
            "#1007F#1P嗯，就像你们想象的一样。\x02\x03",

            "那扇门正是\x01",
            "砸晕德尔斯的犯人……\x02\x03",

            "#1002F猛然打开的门\x01",
            "直接打击到了你的后脑部。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B199")

    ChrTalk(    #687
        0x15,
        (
            "#551F#2P也就是说案件的真相\x01",
            "其实是『不幸的意外』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1D7")

    label("loc_B199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B1D7")

    ChrTalk(    #688
        0x16,
        (
            "#025F#2P也就是说案件的真相\x01",
            "其实是『不幸的意外』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1D7")

    Sleep(400)
    OP_59()
    Fade(1000)
    OP_6D(-2970, 0, 79000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #689
        0x14,
        "咦！？那么……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 180, 800)
    Sleep(400)

    ChrTalk(    #690
        0x14,
        "总之就是说我是无辜的？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 225, 400)
    Sleep(400)

    ChrTalk(    #691
        0xE,
        (
            "唔……\x01",
            "看来是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0x14,
        (
            "呼～真受不了。\x01",
            "终于能无罪释放了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)
    Sleep(400)

    ChrTalk(    #693
        0xB,
        "不过说起来还真是大动干戈呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0xB,
        "为什么你一开始没有自己承认？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #695
        0xB,
        (
            "如果你那样做的话\x01",
            "事情就不会闹得这么大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #696
        0xF,
        "对、对不起……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #697
        0x101,
        (
            "#1016F#3P嗯，话是没错，\x01",
            "能不能就这么饶了他？\x02\x03",

            "到最后他还是\x01",
            "拿出勇气说了出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #698
        0x1A,
        (
            "嗯，身为被害者\x01",
            "我也希望能够原谅他。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #699
        0x1A,
        (
            "因为我们已经知道了\x01",
            "那个过失也不是恶意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #700
        0x1A,
        (
            "当然，希望你开门的时候\x01",
            "能够再小心一点……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x1A, 400)

    ChrTalk(    #701
        0xF,
        "德尔斯先生，真的很对不起。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x14, 400)

    ChrTalk(    #702
        0xF,
        (
            "还有昆茨先生也是。\x01",
            "差点让你背负了这个罪名。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0xF, 400)

    ChrTalk(    #703
        0x14,
        "我倒是没什么。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #704
        0x14,
        (
            "到头来嫌疑还是被洗清了。\x01",
            "这就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #705
        0x17,
        "#031F#3P呼，这件事总算是了结了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #706
        0x105,
        "#040F#4P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B5BB")

    ChrTalk(    #707
        0x15,
        (
            "#050F然后是贝尔夫……\x02\x03",

            "接下来要怎么做\x01",
            "全由你自己来决定。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x15, 400)

    ChrTalk(    #708
        0xF,
        "阿、阿加特先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #709
        0x15,
        (
            "#051F啊啊，好好干啊。\x02\x03",

            "#053F…………以上就是报告内容。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5E9")

    label("loc_B5BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B5E9")

    ChrTalk(    #710
        0x16,
        "#020F……以上就是报告内容，完毕。\x02",
    )

    CloseMessageWindow()

    label("loc_B5E9")


    ChrTalk(    #711
        0xB,
        (
            "诸位游击士……\x01",
            "今天真抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #712
        0xB,
        (
            "一个很过分的不小心\x01",
            "给你们添了这么多麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #713
        0x101,
        (
            "#1000F哪里的话，不用介意啦。\x02\x03",

            "这也是我们的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B69D")

    ChrTalk(    #714
        0x15,
        "#050F那我们就先走了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 400)
    Jump("loc_B6C8")

    label("loc_B69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_B6C8")

    ChrTalk(    #715
        0x16,
        "#020F那我们就先告辞了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x16, 400)

    label("loc_B6C8")

    OP_8C(0xF, 180, 400)

    ChrTalk(    #716
        0xF,
        (
            "真的……\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #717
        0xB,
        "真的很抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #718
        0x14,
        "那么，工作要加油啊！\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_A681 end

    def Function_26_B732(): pass

    label("Function_26_B732")

    OP_8B(0xFE, 0xFFFFFB8C, 0x148CA, 0x190)
    Return()

    # Function_26_B732 end

    def Function_27_B740(): pass

    label("Function_27_B740")

    SetChrPos(0xFE, 5750, 2250, 380, 262)
    OP_8E(0xFE, 0x2C6, 0x0, 0x15E, 0x5DC, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_27_B740 end

    def Function_28_B76D(): pass

    label("Function_28_B76D")

    SetChrPos(0xFE, 6330, 2250, -170, 281)
    OP_8E(0xFE, 0x582, 0x0, 0xFFFFFF42, 0x5DC, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_B76D end

    def Function_29_B79A(): pass

    label("Function_29_B79A")

    OP_8E(0xFE, 0xFFFFFD4E, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF510, 0x0, 0xC6C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF308, 0x0, 0x2526, 0x7D0, 0x0)
    Return()

    # Function_29_B79A end

    def Function_30_B7D7(): pass

    label("Function_30_B7D7")

    OP_8E(0xFE, 0xFFFFFECA, 0x0, 0xFFFFFF42, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6AA, 0x0, 0xA64, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF5C4, 0x0, 0x201C, 0x7D0, 0x0)
    Return()

    # Function_30_B7D7 end

    def Function_31_B814(): pass

    label("Function_31_B814")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_31_B814 end

    def Function_32_B829(): pass

    label("Function_32_B829")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_32_B829 end

    def Function_33_B83E(): pass

    label("Function_33_B83E")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_33_B83E end

    def Function_34_B853(): pass

    label("Function_34_B853")

    OP_90(0xFE, 0xFFFFF060, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_34_B853 end

    def Function_35_B868(): pass

    label("Function_35_B868")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 500, 0, 76980, 255)

    def lambda_B88A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B88A)
    OP_8E(0xFE, 0xFFFFFF1A, 0x0, 0x12CC8, 0x7D0, 0x0)
    Return()

    # Function_35_B868 end

    def Function_36_B8AB(): pass

    label("Function_36_B8AB")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFAEC, 0x0, 0x13902, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_36_B8AB end

    def Function_37_B8DF(): pass

    label("Function_37_B8DF")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF2B8, 0x0, 0x133BC, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_37_B8DF end

    def Function_38_B913(): pass

    label("Function_38_B913")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0x132F4, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_38_B913 end

    def Function_39_B947(): pass

    label("Function_39_B947")

    Call(1, 35)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3B2, 0x0, 0x12E3A, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_39_B947 end

    def Function_40_B97B(): pass

    label("Function_40_B97B")

    Call(1, 35)
    OP_8C(0xFE, 90, 400)
    OP_72(0x6, 0x800)
    OP_70(0x6, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x6)
    OP_71(0x6, 0x800)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF79A, 0x0, 0x12D72, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_40_B97B end

    def Function_41_B9D4(): pass

    label("Function_41_B9D4")

    TurnDirection(0xFE, 0x18, 400)
    Return()

    # Function_41_B9D4 end

    def Function_42_B9DC(): pass

    label("Function_42_B9DC")

    TurnDirection(0xFE, 0x18, 400)
    Return()

    # Function_42_B9DC end

    def Function_43_B9E4(): pass

    label("Function_43_B9E4")

    OP_8C(0x104, 180, 400)
    SetChrChipByIndex(0x104, 10)
    SetChrFlags(0x104, 0x2)
    OP_99(0x104, 0x0, 0x3, 0x4B0)
    Sleep(200)
    OP_99(0x104, 0x3, 0xA, 0x4B0)
    Return()

    # Function_43_B9E4 end

    def Function_44_BA0D(): pass

    label("Function_44_BA0D")

    OP_6D(130, 0, 4860, 1000)
    OP_6D(-170, 0, 2320, 2000)
    Return()

    # Function_44_BA0D end

    SaveToFile()

Try(main)
