from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3117_1 ._SN',
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
        '雷伊',                                 # 9
        '蒂亚利',                               # 10
        '米优',                                 # 11
        '安东尼',                               # 12
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
    )

    DeclNpc(
        X                   = 1070,
        Z                   = 0,
        Y                   = 9970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 0,
        Y                   = 14150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -2590,
        Z                   = 0,
        Y                   = 8420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3650,
        Z                   = 0,
        Y                   = 2680,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -5350,
        TriggerZ            = 0,
        TriggerY            = 4760,
        TriggerRange        = 1000,
        ActorX              = -5350,
        ActorZ              = 500,
        ActorY              = 4760,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5500,
        TriggerZ            = 0,
        TriggerY            = 5390,
        TriggerRange        = 1000,
        ActorX              = 5500,
        ActorZ              = 500,
        ActorY              = 5390,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 1000,
        TriggerY            = 14290,
        TriggerRange        = 1000,
        ActorX              = 4470,
        ActorZ              = 1500,
        ActorY              = 14290,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1750,
        TriggerZ            = 0,
        TriggerY            = 12760,
        TriggerRange        = 1000,
        ActorX              = 1750,
        ActorZ              = 0,
        ActorY              = 12760,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_287",          # 01, 1
        "Function_2_2B7",          # 02, 2
        "Function_3_2DB",          # 03, 3
        "Function_4_7B6",          # 04, 4
        "Function_5_14CE",         # 05, 5
        "Function_6_1572",         # 06, 6
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1EB")
    Jump("loc_201")

    label("loc_1EB")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 4490, 1000, 8220, 0)

    label("loc_201")

    Jump("loc_286")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_224")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -2590, 0, 9570, 270)
    Jump("loc_286")

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_24E")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -2590, 0, 9570, 180)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_286")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_27A")
    SetChrPos(0x8, 5290, 1000, 8740, 0)
    SetChrPos(0x9, -2590, 0, 9570, 270)
    Jump("loc_286")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_286")
    ClearChrFlags(0xB, 0x80)

    label("loc_286")

    Return()

    # Function_0_1DA end

    def Function_1_287(): pass

    label("Function_1_287")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_7B()
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)

    label("loc_2A6")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Return()

    # Function_1_287 end

    def Function_2_2B7(): pass

    label("Function_2_2B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DA")
    OP_8D(0xFE, 4670, 5810, -4590, 550, 1000)
    Jump("Function_2_2B7")

    label("loc_2DA")

    Return()

    # Function_2_2B7 end

    def Function_3_2DB(): pass

    label("Function_3_2DB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A")

    ChrTalk(    #0
        0xFE,
        (
            "呼，终于来到\x01",
            "这里了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "导力虽然停止了，\x01",
            "不过温室总算没什么大碍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "蒂亚利也完成了\x01",
            "最低限度的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "呼，也希望『埃尔赛尤』\x01",
            "那边也能一切顺利。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3DE")

    label("loc_39A")


    ChrTalk(    #4
        0xFE,
        (
            "温室也没事，\x01",
            "暂时可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "总之要准备\x01",
            "重新开始实验了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE")

    Jump("loc_7B2")

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_5E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47D")

    ChrTalk(    #6
        0xFE,
        (
            "我也想要像一个提妲一样\x01",
            "天真可爱的助手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "呼，等温室的实验结束以后要\x01",
            "开始进行导力人偶的开发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "呵呵，模特儿\x01",
            "当然是提妲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DF")

    label("loc_47D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")

    ChrTalk(    #9
        0xFE,
        "啊，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "你们今天看上去也很忙呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_50F")

    label("loc_4BA")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #11
        0xFE,
        (
            "哟，那不是\x01",
            "提妲吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "你们今天看上去也很忙呢。\x02",
    )

    CloseMessageWindow()

    label("loc_50F")


    ChrTalk(    #13
        0x107,
        (
            "#560F啊，是。\x02\x03",

            "我又来帮\x01",
            "爷爷了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "呼，拉赛尔博士\x01",
            "真是有个好助手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "相比之下，\x01",
            "我现在的助手……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #16
        0xFE,
        "……算了，不耍嘴皮子了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "提妲，不好意思。\x01",
            "你回去工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#060F那我先过去了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5DF")

    Jump("loc_7B2")

    label("loc_5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_6D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_643")

    ChrTalk(    #19
        0xFE,
        (
            "世界上有很多\x01",
            "可以研究的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "但是值得研究的东西\x01",
            "却只有很少的一点点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4")

    label("loc_643")


    ChrTalk(    #21
        0xFE,
        (
            "农作物的品种改良\x01",
            "刚刚取得了前期的成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "不过培育一般的\x01",
            "农作物并不有趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "呼，呆在研究室\x01",
            "也找不到灵感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "看来要去\x01",
            "散个步了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6D4")

    Jump("loc_7B2")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_7B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_732")

    ChrTalk(    #25
        0xFE,
        (
            "蒂亚利还没决定\x01",
            "本期的课题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "没办法，只能先把他\x01",
            "当作助手使唤了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B2")

    label("loc_732")


    ChrTalk(    #27
        0xFE,
        (
            "呼，这次的课题\x01",
            "仍然是温室的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "虽然如此，不过是\x01",
            "让蒂亚利一个人在做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "呼，有什么可以有效\x01",
            "利用温室的建议吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7B2")

    TalkEnd(0x8)
    Return()

    # Function_3_2DB end

    def Function_4_7B6(): pass

    label("Function_4_7B6")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7C6")
    OP_A2(0x3)

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_846")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在上半部完成过QST042】\x01",        # 0
            "【◇在上半部没完成过QST042】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_83A"),
        (1, "loc_840"),
        (SWITCH_DEFAULT, "loc_846"),
    )


    label("loc_83A")

    OP_A2(0x3)
    Jump("loc_846")

    label("loc_840")

    OP_A3(0x3)
    Jump("loc_846")

    label("loc_846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_938")

    ChrTalk(    #30
        0xFE,
        (
            "雷伊前辈\x01",
            "终于回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "他之前好像和拉赛尔博士\x01",
            "一起在『埃尔赛尤』上做研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "在、在我管理温室的时候前辈\x01",
            "已经在做这么尖端的研究了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "可、可恶……！！\x01",
            "我也不会输的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "下次的研究\x01",
            "一定要拿出成果来！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_990")

    label("loc_938")


    ChrTalk(    #35
        0xFE,
        (
            "总觉得跟前辈的\x01",
            "差距越来越大了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "我、我下次一定要努力\x01",
            "嗯，导力枪的调整ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    Jump("loc_14CA")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 2)), scpexpr(EXPR_END)), "loc_A21")

    ChrTalk(    #37
        0xFE,
        (
            "总、总之希望雷伊\x01",
            "前辈能平安返回。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "因为导力器不工作了，\x01",
            "所以温室管理也变得困难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "啊，前辈！\x01",
            "请马上回来吧！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0")

    ChrTalk(    #40
        0xFE,
        (
            "雷、雷伊前辈不知道被\x01",
            "带去哪儿了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "所以没办法，\x01",
            "只能让我来做温室的管理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "不过因为导力器不工作了，\x01",
            "所以温室管理也变得困难了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "总、总之希望前辈\x01",
            "早点回来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 7)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC1")

    ChrTalk(    #44
        0x107,
        (
            "#064F那个，说起来……\x02\x03",

            "我们好像在古罗尼山顶\x01",
            "看见过哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #45
        0xFE,
        "古、古罗尼山顶？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1002F嗯……\x02\x03",

            "要不了多久\x01",
            "应该会回来的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #47
        0xFE,
        "这，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "反正不管怎样只要\x01",
            "他平安回来就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_BC1")


    ChrTalk(    #49
        0x101,
        (
            "#1015F嗯，先告诉你一下吧……\x02\x03",

            "那位雷伊先生，\x01",
            "我们在古罗尼山顶看见了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #50
        0xFE,
        "古、古罗尼山顶？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1040F嗯，现在只能\x01",
            "步行了。\x02\x03",

            "虽然可能很花时间，\x01",
            "不过他一定会回来的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #52
        0xFE,
        "这，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "反正不管怎样只要\x01",
            "他平安回来就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB7")

    OP_A2(0x20D2)

    label("loc_CBA")

    OP_A2(0x1)
    Jump("loc_D4D")

    label("loc_CC0")


    ChrTalk(    #54
        0xFE,
        (
            "雷伊前辈被带走了，\x01",
            "只能让我来做温室的管理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "不过因为导力器不工作了，\x01",
            "所以温室管理也变得困难了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "啊，前辈！\x01",
            "请快点回来！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4D")

    Jump("loc_14CA")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_DF8")

    ChrTalk(    #57
        0xFE,
        (
            "课题啊……\x01",
            "选什么好呢…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "啊，米优小姐……\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #60
        0xFE,
        (
            "……咦，我说\x01",
            "我在想什么啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8E")

    label("loc_DF8")


    ChrTalk(    #61
        0xFE,
        "刚才新人来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "有种未经世故的可爱啊～\x01",
            "是个坦率活泼的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "……不，没时间\x01",
            "想这些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "呼，得早点决定\x01",
            "研究课题……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    OP_A2(0x2)

    label("loc_E8E")

    Jump("loc_1067")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EEE")

    ChrTalk(    #65
        0xFE,
        (
            "那个，现在还处在\x01",
            "寻找课题的阶段哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "在决定之前我先\x01",
            "帮前辈做实验。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F21")

    label("loc_EEE")


    ChrTalk(    #67
        0xFE,
        "嘿、嘿～你就是新人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "很、很年轻呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F21")

    Jump("loc_1067")

    label("loc_F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F8F")

    ChrTalk(    #69
        0xFE,
        (
            "呼，得早点决定下一个\x01",
            "研究课题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "好、好像我要被选为\x01",
            "雷伊前辈的助手了，真可怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1001")

    label("loc_F8F")


    ChrTalk(    #71
        0xFE,
        (
            "嗯，下一个课题\x01",
            "选什么好呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "总不能永远给雷伊\x01",
            "前辈做帮手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "再磨磨蹭蹭的话\x01",
            "真的要被选为助手了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1001")

    Jump("loc_1067")

    label("loc_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1067")

    ChrTalk(    #74
        0xFE,
        (
            "因为这里是４层，\x01",
            "所以摇晃地比较厉害一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "总之地震没有造成\x01",
            "设备的损坏真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1067")

    Jump("loc_10B6")

    label("loc_106A")


    ChrTalk(    #76
        0xFE,
        (
            "现在我正在\x01",
            "寻找下一个课题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "如果再有什么事的话\x01",
            "我还会联系协会的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_14CA")

    label("loc_10B9")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #78
        0xFE,
        (
            "哟，好久不见。\x01",
            "还记得我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "瞧，我是蒂亚利啊。\x01",
            "做过运动鞋研究的那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1016F哈哈，放心好了。\x01",
            "我没忘记你。\x02\x03",

            "你是为斯托雷加社工作的吧。\x01",
            "我怎么会忘了呢。\x02\x03",

            "#1000F那蒂亚利先生你\x01",
            "还在做鞋的研究？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "不，托你们的福\x01",
            "研究目的已经达到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "把数据送到斯托雷加社\x01",
            "之后那个工作就完成了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #83
        0xFE,
        (
            "……对了，按照约定我把你的\x01",
            "口信也传达过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "就是『我期待着你们的新产品哦』那句，\x01",
            "我就说是游击士中的爱好者说的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #85
        0x101,
        "#1004F真、真的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "嗯，当然是真的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "斯托雷加的开发者也\x01",
            "非常激动哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "还开玩笑说\x01",
            "『下次做游击士用的吧！』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1008F啊～是玩笑吗～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "哈哈，那我就不知道了。\x01",
            "只不过我觉得是玩笑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "反正因此我的\x01",
            "研究经费也增加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "现在我正在\x01",
            "寻找下一个课题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "下次可能也会\x01",
            "拜托协会帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "到时候也麻烦\x01",
            "你们一如既往地帮我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006F嗯，你就\x01",
            "不用客气了。\x02\x03",

            "#1015F还有，我想不用\x01",
            "我说你也知道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1005F#3S斯托雷加社的委托\x01",
            "我会放在第一位的！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #97
        0xFE,
        "哈、哈哈，我明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142D)
    OP_A2(0x1)

    label("loc_14CA")

    TalkEnd(0x9)
    Return()

    # Function_4_7B6 end

    def Function_5_14CE(): pass

    label("Function_5_14CE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(    #98
        0xFE,
        (
            "老师您在做\x01",
            "什么样的研究呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "米优可能会很有兴趣的～\x02",
    )

    CloseMessageWindow()
    Jump("loc_156E")

    label("loc_151F")


    ChrTalk(    #100
        0xFE,
        "嘿嘿，初次见面～☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "我是实习生\x01",
            "米优～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "能不能让我\x01",
            "找找资料啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_156E")

    TalkEnd(0xA)
    Return()

    # Function_5_14CE end

    def Function_6_1572(): pass

    label("Function_6_1572")

    TalkBegin(0xB)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #103
        0xFE,
        "喵噢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_1572 end

    SaveToFile()

Try(main)
