from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1220   ._SN',
        MapName             = 'Bose',
        Location            = 'T1220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '埃米尔',                               # 9
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
        'ED6_DT07/CH01040 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
    )

    DeclNpc(
        X                   = -1600,
        Z                   = -1000,
        Y                   = 7600,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -670,
        TriggerZ            = -1000,
        TriggerY            = 6680,
        TriggerRange        = 400,
        ActorX              = -1600,
        ActorZ              = 500,
        ActorY              = 7600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_155",          # 02, 2
        "Function_3_16B",          # 03, 3
        "Function_4_1E2",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_10A")
    OP_B1("T1220_n")
    Jump("loc_126")

    label("loc_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_11D")
    OP_B1("T1220_y")
    Jump("loc_126")

    label("loc_11D")

    OP_B1("T1220_n")

    label("loc_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_147")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_154")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_154")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)

    label("loc_154")

    Return()

    # Function_1_F7 end

    def Function_2_155(): pass

    label("Function_2_155")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_155")

    label("loc_16A")

    Return()

    # Function_2_155 end

    def Function_3_16B(): pass

    label("Function_3_16B")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC")
    OP_0D()
    OP_A9(0x46)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD")
    TalkEnd(0x8)
    Return()

    label("loc_1DD")

    Call(0, 4)
    Return()

    # Function_3_16B end

    def Function_4_1E2(): pass

    label("Function_4_1E2")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(    #0
        0x8,
        (
            "定期船和货车都停开了，\x01",
            "看来还没恢复原状呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "这里的商品几乎\x01",
            "都是从柏斯运来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "话虽如此，我们\x01",
            "可是束手无策啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "呼，只好叹气了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2E3")

    label("loc_28F")


    ChrTalk(    #4
        0x8,
        (
            "这里的商品几乎\x01",
            "都是从柏斯运来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "搬运车不能动的话，\x01",
            "要卖的东西也快光了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E3")

    Jump("loc_682")

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")

    ChrTalk(    #6
        0x8,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "总之还在\x01",
            "勉强继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "导力器不能动了，\x01",
            "柏斯好像也是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "搬运车不能动的话，\x01",
            "我们的商品也很快要断货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "呼，怎么办呢……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_405")

    label("loc_39C")


    ChrTalk(    #11
        0x8,
        (
            "总之还在\x01",
            "勉强继续营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "导力器不能动了，\x01",
            "柏斯好像也是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "一定发生很大的\x01",
            "骚乱了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_405")

    Jump("loc_682")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_46C")

    ChrTalk(    #14
        0x8,
        (
            "似乎有很多人\x01",
            "为村子捐款呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "真是太感谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "终于感觉村子\x01",
            "恢复往日的明朗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4E3")

    ChrTalk(    #17
        0x8,
        (
            "果树园的重建\x01",
            "似乎正在进行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "讨论那边\x01",
            "不知道是否顺利呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "如果不齐心合力，\x01",
            "复兴就只是梦想啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_5CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_546")

    ChrTalk(    #20
        0x8,
        (
            "现在看到军服\x01",
            "还是会感到不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "……战争时期的事\x01",
            "一直在脑子里挥之不去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8")

    label("loc_546")


    ChrTalk(    #22
        0x8,
        (
            "王国军的士兵们\x01",
            "好像撤退了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "虽然他们并没错，\x01",
            "但是看到军服还是会不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "……战争时期的事\x01",
            "一直在脑子里挥之不去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5C8")

    Jump("loc_682")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_682")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_619")

    ChrTalk(    #25
        0x8,
        "果树园的损害很严重啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "今年的收获\x01",
            "恐怕是不行了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_682")

    label("loc_619")


    ChrTalk(    #27
        0x8,
        "呀，欢迎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "虽然火已经灭了，\x01",
            "但果树园的损害很严重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "……我们拉文努村\x01",
            "今后会怎样呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_682")

    TalkEnd(0x8)
    Return()

    # Function_4_1E2 end

    SaveToFile()

Try(main)
