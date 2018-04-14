from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T5110_1 ._SN',
        MapName             = 'Other',
        Location            = 'T5110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60025",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T5110   ._SN',
            'ED6_DT21/T5110_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_30F",          # 03, 3
        "Function_4_558",          # 04, 4
        "Function_5_ACB",          # 05, 5
        "Function_6_E2D",          # 06, 6
        "Function_7_12D8",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_24E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_143")
    Jump("loc_185")

    label("loc_143")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15F")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_15F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_185")

    label("loc_17B")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F")
    OP_A2(0x0)

    ChrTalk(    #0
        0x9,
        (
            "#843F来了吗，艾丝蒂尔。\x02\x03",

            "#840F那就马上开始说明演习内容吧。\x01",
            "请坐到对面的位子上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243")

    label("loc_20F")


    ChrTalk(    #1
        0x9,
        (
            "#840F赶快，演习要开始了。\x01",
            "请坐到对面的位子上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Jump("loc_30E")

    label("loc_24E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2")
    OP_A2(0x0)

    ChrTalk(    #2
        0x9,
        (
            "#840F啊，是艾丝蒂尔吗。\x02\x03",

            "请马上整理好装备\x01",
            "然后到一楼去吧。\x02\x03",

            "距离演习开始\x01",
            "已经没有多少时间了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B")

    label("loc_2C2")


    ChrTalk(    #3
        0x9,
        (
            "#840F先去自己的房间\x01",
            "整理好装备吧。\x02\x03",

            "离演习开始的时间\x01",
            "已经没多久了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B")

    TalkEnd(0x9)

    label("loc_30E")

    Return()

    # Function_2_AC end

    def Function_3_30F(): pass

    label("Function_3_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_43E")
    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A6")
    Jump("loc_3E8")

    label("loc_3A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C2")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E8")

    label("loc_3C2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DE")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E8")

    label("loc_3DE")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E8")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    ChrTalk(    #4
        0x8,
        (
            "#810F艾丝蒂尔，\x01",
            "快坐到我旁边来。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Jump("loc_557")

    label("loc_43E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 7)), scpexpr(EXPR_END)), "loc_4A4")

    ChrTalk(    #5
        0x8,
        (
            "#810F赶快准备好，\x01",
            "然后到一楼集合吧。\x02\x03",

            "克鲁茨前辈很讲究守时，\x01",
            "如果迟到一定会被骂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_554")

    label("loc_4A4")

    OP_A2(0x1037)

    ChrTalk(    #6
        0x8,
        (
            "#814F啊，艾丝蒂尔。\x01",
            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1000F啊……还要再回去整备一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#810F是吗……\x01",
            "好，那就快点吧。\x02\x03",

            "那么，艾丝蒂尔。\x01",
            "待会儿见啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1006F嗯，待会儿见！\x02",
    )

    CloseMessageWindow()

    label("loc_554")

    TalkEnd(0x8)

    label("loc_557")

    Return()

    # Function_3_30F end

    def Function_4_558(): pass

    label("Function_4_558")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_5B7")

    ChrTalk(    #10
        0xA,
        (
            "先听听克鲁茨前辈\x01",
            "要说些什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "他好像有什么东西\x01",
            "想交给你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DD")

    label("loc_5B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_687")

    ChrTalk(    #12
        0xA,
        "呀，早上好啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "早上的锻炼也很辛苦啊，\x01",
            "在这里都听得到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "导力工房暂时还无法使用，\x01",
            "不过在你们出发前就可以恢复正常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "想调整导力器或购买结晶回路的话\x01",
            "等一会儿再来就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DD")

    label("loc_687")


    ChrTalk(    #16
        0xA,
        (
            "导力工房现在还在\x01",
            "进行开店准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "不过在你们出发之前肯定\x01",
            "可以开张，放心好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DD")

    TalkEnd(0xA)
    Return()

    label("loc_6E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F5")
    Call(1, 7)
    Return()

    label("loc_6F5")

    OP_A2(0x1007)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "买东西\x01",          # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_762")
    OP_A9(0xFA)
    Jump("loc_764")

    label("loc_762")

    OP_A9(0xFD)

    label("loc_764")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_76D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_792")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_787")
    OP_A9(0xFB)
    Jump("loc_789")

    label("loc_787")

    OP_A9(0xFE)

    label("loc_789")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_792")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A3")
    TalkEnd(0xA)
    Return()

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #18
        0xA,
        "演习怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "需要整备的时候\x01",
            "就回这里来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC7")

    label("loc_7E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_B9(0x0, 0x6E)"), scpexpr(EXPR_EXEC_OP, "OP_B9(0x9, 0x6E)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_842")

    ChrTalk(    #20
        0xA,
        (
            "嗯，你们已经可以使用\x01",
            "回复魔法了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "那么，你们俩\x01",
            "小心一些出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC7")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x258, 0x0)"), scpexpr(EXPR_END)), "loc_974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8AD")

    ChrTalk(    #22
        0xA,
        (
            "把『ＨＰ１』的结晶回路装备上\x01",
            "就可以使用回复魔法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "有了它的话\x01",
            "就万无一失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_971")

    label("loc_8AD")


    ChrTalk(    #24
        0xA,
        (
            "噢，看来你们已经顺利\x01",
            "合成了结晶回路啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "把它镶嵌到导力器中\x01",
            "就可以使用回复魔法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        "那样的话就算是准备万全了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "好了，克鲁茨前辈还在外边等着呢。\x01",
            "赶快把结晶回路镶嵌好就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_971")

    Jump("loc_AC7")

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A18")

    ChrTalk(    #28
        0xA,
        "啊，难道不知道该怎么做吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        "真是拿你没办法……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "只要合成结晶回路『ＨＰ１』\x01",
            "就可以了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "把它镶嵌到导力器中\x01",
            "有了它就可以施展回复魔法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC7")

    label("loc_A18")


    ChrTalk(    #32
        0xA,
        "回复魔法的名字是『回复术』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "查看游击士手册中的『魔法表』\x01",
            "就可以知道它所需要的回路属性值了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "想合成结晶回路的时候，\x01",
            "在[改造·换钱]中选择[结晶回路]就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_AC7")

    TalkEnd(0xA)
    Return()

    # Function_4_558 end

    def Function_5_ACB(): pass

    label("Function_5_ACB")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBB")
    OP_A2(0x1035)

    ChrTalk(    #35
        0xB,
        "哎呀，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xB,
        "怎么样？吃饱了没有？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1008F嘿嘿嘿，已经吃撑了。\x02\x03",

            "实在太好吃了，\x01",
            "不知不觉就吃好多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xB,
        "呵呵，那就好㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "今天的训练\x01",
            "好像是很重要的演习呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "拿出干劲\x01",
            "努力上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1006F嗯！\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF4")

    label("loc_BBB")


    ChrTalk(    #42
        0xB,
        "训练要加油啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "我会准备好美味的晚餐\x01",
            "等你们的㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF4")

    TalkEnd(0xB)
    Return()

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4D")

    ChrTalk(    #44
        0xB,
        "啊，快点过去坐吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "克鲁茨先生和亚妮拉丝\x01",
            "一直在等你。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    label("loc_C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C65")
    Call(1, 6)
    TalkEnd(0xB)
    Return()

    label("loc_C65")

    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_C82")
    OP_A9(0xFC)
    Jump("loc_C84")

    label("loc_C82")

    OP_A9(0xFF)

    label("loc_C84")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_C8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9E")
    TalkEnd(0xB)
    Return()

    label("loc_C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D23")
    OP_A2(0x2)

    ChrTalk(    #46
        0xB,
        "哎呀，你们两人辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "有什么需要的东西\x01",
            "赶快回宿舍休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "我和罗伯特先生\x01",
            "会一直在这里等着你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D66")

    label("loc_D23")


    ChrTalk(    #49
        0xB,
        (
            "有什么需要的东西\x01",
            "赶快回宿舍休息吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        "那么，演习时加油吧！\x02",
    )

    CloseMessageWindow()

    label("loc_D66")

    Jump("loc_E29")

    label("loc_D69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC5, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_DD7")

    ChrTalk(    #51
        0xB,
        (
            "在情况危险的时候\x01",
            "别忘了吃些料理，然后休息一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xB,
        (
            "有干劲虽然很好，\x01",
            "但一定不要太勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_E29")

    ChrTalk(    #53
        0xB,
        "快点快点，克鲁茨先生已经在等着了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "快点去听他说明演习内容吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E29")

    label("loc_E29")

    TalkEnd(0xB)
    Return()

    # Function_5_ACB end

    def Function_6_E2D(): pass

    label("Function_6_E2D")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 22220, 0, 12120, 90)
    SetChrPos(0x10A, 21720, 0, 12890, 90)
    OP_8C(0xB, 270, 0)
    OP_6D(23050, 0, 12920, 0)
    OP_0D()

    ChrTalk(    #55
        0xB,
        (
            "今天的演习\x01",
            "好像要比平时更严酷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "我现在把这个简单料理\x01",
            "的配方教给你吧㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #57
        "\x07\x00得到了\x1F\x0D\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_3E(0x20D, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1E)"), scpexpr(EXPR_END)), "loc_F0C")
    Jump("loc_F3A")

    label("loc_F0C")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #58
        "\x06\x07\x02大自然恩惠之水\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_F3A")

    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #59
        0xB,
        "对了，食材也别忘记了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #60
        "\x06\x07\x00得到了\x07\x02#20I食材的组合\x07\x00。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_3E(0x396, 10)
    OP_3E(0x399, 10)
    OP_3E(0x39B, 10)
    OP_3E(0x394, 10)
    OP_3E(0x393, 10)
    OP_3E(0x390, 10)
    OP_3E(0x3A8, 2)

    ChrTalk(    #61
        0x10A,
        (
            "#0814F现在就用手里的食材\x01",
            "试着制作料理如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        (
            "嗯，普通料理所需的食材\x01",
            "都很容易买到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        "不过有些料理所需的食材…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "需要打倒魔兽后才能得到，\x01",
            "光是收集就很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1016F确、确实……\x01",
            "有很多食材是非常稀少的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        (
            "#0817F嗯～原来如此。\x01",
            "天上是不会掉馅饼的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "有关料理的详细说明\x01",
            "在游击士手册中就有记载，\x01",
            "有时间的话仔细读读吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "那么，你们两个～\x01",
            "演习时要加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1006F嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10A,
        "#1310F制作料理…马上来试试吧！\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #71
        (
            "\x07\x05※品尝餐厅、酒馆的『推荐菜式』，\x01",
            "　或是使用道具中的『携带料理』后，\x01",
            "　都会在料理手册中自动添加新料理配方。\x02\x03",

            "※有了食材和配方后，只要食材足够的话，\x01",
            "　就可以随时制作料理了。\x02\x03",

            "※料理手册的打开方法∶在主菜单的［Items］\x01",
            "  项中的[书籍]类别中选择『料理手册』。\x01",
            "  另外点击画面右下方的图标(红)也可以打开。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0xC5, 0x1, 0x4)
    FadeToBright(300, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_6_E2D end

    def Function_7_12D8(): pass

    label("Function_7_12D8")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 24620, 0, 4960, 90)
    SetChrPos(0x10A, 24060, 0, 5730, 90)
    OP_8C(0xA, 270, 0)
    OP_6D(24720, 0, 5730, 0)
    OP_0D()

    ChrTalk(    #72
        0xA,
        (
            "哟，看来你们两个都已经\x01",
            "装备上新型导力器了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "手册中记载的新型结晶回路\x01",
            "和魔法目录\x01",
            "已经读过了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "基本使用方法和原来的导力器\x01",
            "没什么不同，但具体性能还是有区别的，\x01",
            "最好仔细熟悉一下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "在正式使用导力器之前\x01",
            "先来复习一下相关的知识吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "有关导力器的知识，\x01",
            "如果有什么内容忘记了可以问我。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_144C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BA3")
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x18\x07\x05想询问什么内容呢？\x02",
    )

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        155,
        0,
        (
            "【导力器】\x01",          # 0
            "【导力魔法】\x01",        # 1
            "【结晶回路】\x01",        # 2
            "【耀晶片】\x01",          # 3
            "【结晶孔强化】\x01",      # 4
            "【放弃】\x01",            # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1524"),
        (1, "loc_1687"),
        (2, "loc_181F"),
        (3, "loc_1965"),
        (4, "loc_1A65"),
        (5, "loc_1B8E"),
        (SWITCH_DEFAULT, "loc_1B9E"),
    )


    label("loc_1524")


    ChrTalk(    #78
        0xA,
        (
            "所谓的导力器，\x01",
            "即是可以通过镶嵌的结晶回路\x01",
            "而发挥出各种效能的机械。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "这里所说的导力器是一种\x01",
            "可以提高身体能力，并可以施展出魔法\x01",
            "的『战术导力器』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "战术导力器都是根据使用者量身定做，\x01",
            "因为每个人的战术导力器\x01",
            "具体构造都是不同的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        (
            "说具体一点，就是结晶孔属性\x01",
            "和结晶链都各不相同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "要想发挥出导力器的最大效力\x01",
            "就必须熟悉自己导力器的特性。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9E")

    label("loc_1687")


    ChrTalk(    #83
        0xA,
        (
            "所谓的导力魔法，\x01",
            "就是需要通过『战术导力器』\x01",
            "而施展的魔法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "因为『导力魔法』这个名字比较拗口，\x01",
            "因此大家一般都简称它为『魔法』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "要想使用魔法的话\x01",
            "就必须先到工房合成结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "把合成好的结晶回路镶嵌到导力器中\x01",
            "就可以施展出各种各样的魔法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "所以，可以使用的魔法种类\x01",
            "会因导力器镶嵌结晶回路的属性不同\x01",
            "而发生改变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "如果想使用水属性的魔法，\x01",
            "在导力器中镶嵌水属性的\x01",
            "结晶回路就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9E")

    label("loc_181F")


    ChrTalk(    #89
        0xA,
        (
            "所谓的结晶回路，\x01",
            "就是用耀晶片合成的回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "结晶回路不仅能决定\x01",
            "可以使用的魔法，还会提高\x01",
            "装备者的自身能力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "结晶回路要镶嵌到导力器的结晶孔\x01",
            "之后才能发挥效果，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "有些结晶孔只能镶嵌特定属性的结晶\x01",
            "回路，其他属性的回路无法镶嵌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "另外，有些高级的结晶回路\x01",
            "只能镶嵌在强化后的结晶孔里，\x01",
            "这一点也请注意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9E")

    label("loc_1965")


    ChrTalk(    #94
        0xA,
        (
            "所谓的耀晶片就是魔兽掉落的\x01",
            "七耀石的碎片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "因颜色的不同，分为#56I地·#57I水·#58I火·#59I风·\x01",
            "#62I时·#60I空·#61I幻……这７个种类。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "耀晶片在很多地方都可以\x01",
            "直接换钱，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "最好还是到工房利用它们\x01",
            "来合成强力的结晶回路\x01",
            "或强化导力孔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9E")

    label("loc_1A65")


    ChrTalk(    #98
        0xA,
        (
            "新型导力器的特征之一\x01",
            "就是结晶孔的强化程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "新型导力器可以镶嵌\x01",
            "很多种性能超群的\x01",
            "结晶回路，不过…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "要想镶嵌那些强力结晶回路的话\x01",
            "首先要将结晶孔进行强化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "另外，在强化结晶孔的同时，\x01",
            "自身的ＥＰ最大值也会增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "虽然这么做需要消费不少耀晶片，\x01",
            "但如果数量足够的话一定要试试看！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B9E")

    label("loc_1B8E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_1B9E")

    label("loc_1B9E")

    OP_56(0x0)
    Jump("loc_144C")

    label("loc_1BA3")


    ChrTalk(    #103
        0xA,
        (
            "那么，说明就到此为止，\x01",
            "接下来赶快去做演习的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "在战斗前最好先准备好\x01",
            "回复类的魔法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "你们应该已经知道使用\x01",
            "回复魔法需要哪种结晶回路了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "如果不知道的话就查看一下手册中\x01",
            "的说明，尽快合成出来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC5, 0x1, 0x8)
    OP_28(0xC5, 0x1, 0x10)
    OP_28(0xC5, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_7_12D8 end

    SaveToFile()

Try(main)
