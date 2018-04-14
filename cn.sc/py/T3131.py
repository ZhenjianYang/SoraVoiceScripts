from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '贝恩',                                 # 9
        '乌尔斯',                               # 10
        '兰达老人',                             # 11
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
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
    )

    DeclNpc(
        X                   = -2470,
        Z                   = -1000,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = -1000,
        Y                   = 5320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -450,
        Z                   = -650,
        Y                   = 2280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_146",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_1A9",          # 02, 2
        "Function_3_1CD",          # 03, 3
        "Function_4_1D2",          # 04, 4
        "Function_5_B68",          # 05, 5
        "Function_6_10DF",         # 06, 6
    )


    def Function_0_146(): pass

    label("Function_0_146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_150")
    Jump("loc_173")

    label("loc_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_15A")
    Jump("loc_173")

    label("loc_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_164")
    Jump("loc_173")

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_16E")
    Jump("loc_173")

    label("loc_16E")

    SetChrFlags(0xA, 0x80)

    label("loc_173")

    Return()

    # Function_0_146 end

    def Function_1_174(): pass

    label("Function_1_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)

    label("loc_1A8")

    Return()

    # Function_1_174 end

    def Function_2_1A9(): pass

    label("Function_2_1A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CC")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 2000)
    Jump("Function_2_1A9")

    label("loc_1CC")

    Return()

    # Function_2_1A9 end

    def Function_3_1CD(): pass

    label("Function_3_1CD")

    Call(0, 4)
    Return()

    # Function_3_1CD end

    def Function_4_1D2(): pass

    label("Function_4_1D2")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    OP_A9(0x9B)
    TalkEnd(0x8)
    Return()

    label("loc_1EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200")
    TalkEnd(0x8)
    Return()

    label("loc_200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20D")
    OP_A2(0x0)

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过任务【新食材的收集】】\x01",        # 0
            "【◇没完成过任务【新食材的收集】】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28D"),
        (1, "loc_293"),
        (SWITCH_DEFAULT, "loc_299"),
    )


    label("loc_28D")

    OP_A2(0x0)
    Jump("loc_299")

    label("loc_293")

    OP_A3(0x0)
    Jump("loc_299")

    label("loc_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_783")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_37E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A")

    ChrTalk(    #0
        0x8,
        (
            "你们也看见过\x01",
            "那个浮游物体了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "听说那东西的上面\x01",
            "有个城镇呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "简直像童话中的世界一样啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_37B")

    label("loc_32A")


    ChrTalk(    #3
        0x8,
        (
            "听说那个浮游物体的上面\x01",
            "有个城镇一样的东西呢\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "简直像童话中的世界一样啊。\x02",
    )

    CloseMessageWindow()

    label("loc_37B")

    Jump("loc_780")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416")

    ChrTalk(    #5
        0x8,
        (
            "虽然空调不能用了，\x01",
            "但正常营业还是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "毕竟这家店的精髓\x01",
            "是明火烹调的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "就算导力没有了\x01",
            "也不会受太大的影响。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_45D")

    label("loc_416")


    ChrTalk(    #8
        0x8,
        "但正常营业还是没问题的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "毕竟这家店的精髓\x01",
            "是明火烹调的料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45D")

    Jump("loc_780")

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_53D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4C7")

    ChrTalk(    #10
        0x8,
        (
            "不会再发生地震了…\x01",
            "这真是个好消息啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "我的原则是——\x01",
            "只要是好事就绝不怀疑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53A")

    label("loc_4C7")

    TurnDirection(0x8, 0xA, 0)

    ChrTalk(    #12
        0x8,
        (
            "不管怎样，\x01",
            "不会再发生地震了…\x01",
            "好消息是绝对不会有差错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "老爷爷想得太多，\x01",
            "所以脑袋秃得更快了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_53A")

    Jump("loc_780")

    label("loc_53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_608")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5A8")

    ChrTalk(    #14
        0x8,
        (
            "互不侵犯条约的签字仪式\x01",
            "似乎也快到了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "要是从共和国来的客人\x01",
            "因此而增多就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_605")

    label("loc_5A8")


    ChrTalk(    #16
        0x8,
        (
            "嗯，听说互不侵犯条约的\x01",
            "签字仪式就要到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "真期待共和国的客人\x01",
            "会因此而增多啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_605")

    Jump("loc_780")

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_6CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_65F")

    ChrTalk(    #18
        0x8,
        (
            "老爷爷的孙女都已经到了\x01",
            "能工作的年龄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "所以我也都\x01",
            "老了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C8")

    label("loc_65F")


    ChrTalk(    #20
        0x8,
        (
            "呼～兰达爷爷的孙女\x01",
            "都已经到了可以工作的年龄了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "呜呼，看来看来，我也\x01",
            "快要变成一个老头子了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6C8")

    Jump("loc_780")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_726")

    ChrTalk(    #22
        0x8,
        (
            "尽管如此\x01",
            "地震真是好久没遇到了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "还好哪里都没有\x01",
            "出现人员伤亡。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_780")

    label("loc_726")


    ChrTalk(    #24
        0x8,
        "噢，累了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "我们这里有可以消除疲劳\x01",
            "的特制料理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "有兴趣的话来试试吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_780")

    Jump("loc_81F")

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7E3")

    ChrTalk(    #27
        0x8,
        (
            "现在的情况虽然很糟糕，\x01",
            "但也只有努力度过难关了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "好啦～大家一起\x01",
            "加油努力吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81F")

    label("loc_7E3")


    ChrTalk(    #29
        0x8,
        (
            "肚子饿了的时候\x01",
            "随时欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "那么，\x01",
            "继续加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F")

    Jump("loc_B64")

    label("loc_822")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8)

    ChrTalk(    #31
        0x8,
        "噢！我还以为是谁呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "这不是帮我找到苦西红柿\x01",
            "的游击士们吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1011F啊，您还记得我们吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "当然记得了！\x01",
            "你简直就是我的恩人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "我们的『苦西红柿料理』\x01",
            "现在可是大受欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1004F哎哎………………！？\x02\x03",

            "#1016F……不、不会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #37
        0x107,
        (
            "#064F嗯，是真的哦。\x02\x03",

            "中央工房的人\x01",
            "几乎都来吃过了。\x02\x03",

            "#561F听说大家都是从营养学的角度\x01",
            "考虑才会选它的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_A20")

    label("loc_9C2")


    ChrTalk(    #38
        0x8,
        (
            "哈哈哈～没有骗人的啦。\x01",
            "特别是在研究员群体中最受好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "在疲劳的时候吃这个\x01",
            "很管用的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A20")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        "#1007F嗯……还是很难理解呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "噢，难得来了，\x01",
            "不如来尝尝最新的料理吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        "当然是我请客！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABB")

    def lambda_AB3():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AB3)

    label("loc_ABB")

    TurnDirection(0x101, 0x8, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00得到了\x1F\x99\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x199, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #44
        0x8,
        (
            "吃了营养十足的料理\x01",
            "今后也要继续加油啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "一定会精力十足，\x01",
            "以后也会充满干劲！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x1426)

    label("loc_B64")

    TalkEnd(0x8)
    Return()

    # Function_4_1D2 end

    def Function_5_B68(): pass

    label("Function_5_B68")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C30")

    ChrTalk(    #46
        0xFE,
        (
            "中央工房为了恢复研究\x01",
            "也一直在努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "露依赛那家伙最近\x01",
            "早上很早就会出去工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "结果她的妹妹就\x01",
            "只会给我添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "……这么一想的话，\x01",
            "导力停止现象还真是讨厌呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_C98")

    label("loc_C30")


    ChrTalk(    #50
        0xFE,
        (
            "仔细想想的话，我会照顾她的妹妹，\x01",
            "也全是因为这次的异变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "嗯，换种眼光看的话，\x01",
            "影响真是很大呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C98")

    Jump("loc_10DB")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_D98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3B")

    ChrTalk(    #52
        0xFE,
        (
            "仔细想想，我们的店里\x01",
            "并没有导力式的器具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "所以今天还是可以\x01",
            "像平时一样正常营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "呼～本来以为会停业休息\x01",
            "还稍微期待了一下呢…\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D95")

    label("loc_D3B")


    ChrTalk(    #55
        0xFE,
        (
            "仔细想想，我们的店里\x01",
            "并没有导力式的器具。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "所以今天还是可以\x01",
            "像平时一样正常营业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D95")

    Jump("loc_10DB")

    label("loc_D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_DF1")

    ChrTalk(    #57
        0xFE,
        (
            "乌缇总是一个人\x01",
            "留在家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "对那种年龄的孩子来说\x01",
            "肯定很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E4C")

    label("loc_DF1")


    ChrTalk(    #59
        0xFE,
        (
            "呼～等休息时间到了以后\x01",
            "还要去露依赛家里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "留下看家的乌缇\x01",
            "也许现在都已经饿了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_E4C")

    Jump("loc_10DB")

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(    #61
        0xFE,
        (
            "她出外工作的时候是谁\x01",
            "替她照看妹妹？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "还不都是我嘛！\x02",
    )

    CloseMessageWindow()
    Jump("loc_F4E")

    label("loc_E9D")


    ChrTalk(    #63
        0xFE,
        (
            "露依赛也真是的，\x01",
            "动不动就要出差呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "这次听说是要去雷斯顿要塞\x01",
            "修整飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "等一下…\x01",
            "仔细想想的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "她出外工作的时候是谁\x01",
            "替她照看妹妹？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "还不都是我嘛！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F4E")

    Jump("loc_10DB")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_FB2")

    ChrTalk(    #68
        0xFE,
        (
            "我店里的盘子好像\x01",
            "叠了很高呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "这样不管的话，\x01",
            "再有地震可就全要摔碎了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF3")

    label("loc_FB2")


    ChrTalk(    #70
        0xFE,
        (
            "呼，太好了。\x01",
            "餐具全都没摔坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "多亏平时整理\x01",
            "得好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_FF3")

    Jump("loc_10DB")

    label("loc_FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1055")

    ChrTalk(    #72
        0xFE,
        (
            "我的女朋友在中央工房\x01",
            "工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "刚才的地震\x01",
            "没有造成重大伤亡算是万幸……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DB")

    label("loc_1055")


    ChrTalk(    #74
        0xFE,
        (
            "呼，比想象中摇动得更强啊，\x01",
            "还真吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "对了，露依赛\x01",
            "好像说过今天要去工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "嗯，中央工房没有\x01",
            "受到灾害再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_10DB")

    TalkEnd(0x9)
    Return()

    # Function_5_B68 end

    def Function_6_10DF(): pass

    label("Function_6_10DF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_11DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117A")

    ChrTalk(    #77
        0xFE,
        (
            "但那浮游物体…\x01",
            "好像连工房的人也很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "呵呵～未知物体\x01",
            "本来就是研究者的最爱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "……不过，这么悠闲\x01",
            "真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_11DA")

    label("loc_117A")


    ChrTalk(    #80
        0xFE,
        (
            "但那浮游物体…\x01",
            "好像连工房的人也很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "说心里话，难道研究\x01",
            "真的不会因此而受影响吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DA")

    Jump("loc_1671")

    label("loc_11DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1282")

    ChrTalk(    #82
        0xFE,
        (
            "其实老板也很想用\x01",
            "导力烤炉的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "但刚开业的时候资金有限，\x01",
            "买不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "没想到现在却因祸得福，\x01",
            "可以继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "果然是世事\x01",
            "难料啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_12DC")

    label("loc_1282")


    ChrTalk(    #86
        0xFE,
        (
            "老板在刚开店的时候很穷，\x01",
            "连导力炉都买不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "不过现在却因祸得福，\x01",
            "可以照常营业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DC")

    Jump("loc_1671")

    label("loc_12DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_13DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1361")

    ChrTalk(    #88
        0xFE,
        (
            "拉赛尔那老家伙现在肯定\x01",
            "还在继续他的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "地震什么的也根本不能\x01",
            "打断他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "嗯，果然是个\x01",
            "一根筋呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D8")

    label("loc_1361")


    ChrTalk(    #91
        0xFE,
        (
            "安全宣言虽然发表了，\x01",
            "但还是不能放心…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "地震不会再发生了什么的，\x01",
            "这种事很难确保吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "嗯……果然很可疑。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_13D8")

    Jump("loc_1671")

    label("loc_13DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1444")

    ChrTalk(    #94
        0xFE,
        (
            "嗯，果然牵连到\x01",
            "和诸国的关系啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "选择保持外交往来，\x01",
            "女王陛下真是很有先见之明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14FB")

    label("loc_1444")


    ChrTalk(    #96
        0xFE,
        (
            "即使如此，导力器的\x01",
            "出货仍然很受好评。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "不但国内状况十分稳定，\x01",
            "而且输出量也增加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "嗯，果然牵连到\x01",
            "和诸国的关系啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "选择保持外交往来，\x01",
            "女王陛下真是很有先见之明。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_14FB")

    Jump("loc_1671")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_15B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1554")

    ChrTalk(    #100
        0xFE,
        (
            "呼～我的孙女是个\x01",
            "粗心大意的孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "一定又会搞出什么乱子吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B1")

    label("loc_1554")


    ChrTalk(    #102
        0xFE,
        (
            "我孙女米优现在\x01",
            "在中央工房帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "不知道她能不能把工作干好，\x01",
            "我瞎担心也是没用啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_15B1")

    Jump("loc_1671")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1671")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1608")

    ChrTalk(    #104
        0xFE,
        (
            "最近我的孙女\x01",
            "也一直频繁出入中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "真让人放心不下啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1671")

    label("loc_1608")


    ChrTalk(    #106
        0xFE,
        (
            "算啦，这种程度的摇晃\x01",
            "应该还不至于影响到中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "因为地震事件，\x01",
            "出现了接连不断的受害事件。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1671")

    TalkEnd(0xA)
    Return()

    # Function_6_10DF end

    SaveToFile()

Try(main)
