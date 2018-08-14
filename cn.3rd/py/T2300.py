from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2300.x',
        MapIndex            = 86,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '玛诺利亚间道方向',                     # 9
        '梅威海道方向',                         # 10
        '目标用照相机',                         # 11
        '卢西亚',                               # 12
        '库拉茨',                               # 13
        '萨蒂',                                 # 14
        '',                                     # 15
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01260 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01260P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37840,
        Z                   = -50,
        Y                   = 17810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 38170,
        Z                   = -20,
        Y                   = 18890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = 37770,
        TriggerZ            = -10,
        TriggerY            = 19530,
        TriggerRange        = 1000,
        ActorX              = 37770,
        ActorZ              = 1800,
        ActorY              = 19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_206",          # 00, 0
        "Function_1_293",          # 01, 1
        "Function_2_2AB",          # 02, 2
        "Function_3_E50",          # 03, 3
        "Function_4_211A",         # 04, 4
        "Function_5_2368",         # 05, 5
        "Function_6_2AA2",         # 06, 6
        "Function_7_2AE3",         # 07, 7
        "Function_8_2B29",         # 08, 8
        "Function_9_2C73",         # 09, 9
        "Function_10_2C77",        # 0A, 10
        "Function_11_2C7B",        # 0B, 11
    )


    def Function_0_206(): pass

    label("Function_0_206")

    OP_72(0x402, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x1002, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_255")
    SetChrFlags(0x15, 0x80)
    SetChrPos(0x13, 4510, 6000, -1100, 90)
    SetChrPos(0x14, 4510, 6000, -100, 90)
    Jump("loc_270")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_25F")
    Jump("loc_270")

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_269")
    Jump("loc_270")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_270")

    label("loc_270")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_292")
    OP_A3(0x2504)
    Event(0, 5)

    label("loc_292")

    Return()

    # Function_0_206 end

    def Function_1_293(): pass

    label("Function_1_293")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x23004B)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_293 end

    def Function_2_2AB(): pass

    label("Function_2_2AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_71A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 5)), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_3D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_375")
    OP_4A(0x14, 255)

    ChrTalk(    #0
        0xFE,
        "悬崖边上、悬崖边上……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "波利的谜题，\x01",
            "真是好难哦～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_343")

    ChrTalk(    #2
        0x14,
        "#823F……快干活啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_36E")

    label("loc_343")


    NpcTalk(    #3
        0x14,
        "男人",
        "#823F……快干活啦。\x02",
    )

    Jump("loc_36D")

    label("loc_36D")

    CloseMessageWindow()

    label("loc_36E")

    OP_4B(0x14, 255)
    Jump("loc_3D1")

    label("loc_375")


    ChrTalk(    #4
        0xFE,
        "悬崖边上、悬崖边上……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "明明是幸福之石，\x01",
            "为什么会在悬崖边上呢～？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3D1")

    Jump("loc_4A9")

    label("loc_3D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_449")

    ChrTalk(    #6
        0xFE,
        (
            "要是像格兰赛尔的百货店那样，\x01",
            "能有很多人来的地方就好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "卢西亚会热烈欢迎大家的⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A9")

    label("loc_449")


    ChrTalk(    #8
        0xFE,
        "没有客人来啊～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "要是像格兰赛尔的百货店一样，\x01",
            "会有很多人来就好了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4A9")

    Jump("loc_717")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_60D")

    ChrTalk(    #10
        0xFE,
        "咦～，是玛丽。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "波利呢？\x01",
            "你们没在一起吗～？\x02",
        )
    )

    Jump("loc_501")

    label("loc_501")

    CloseMessageWindow()

    ChrTalk(    #12
        0x14E,
        (
            "#1713F嗯、嗯……\x02\x03",

            "#1712F波利在和\x01",
            "克拉姆他们一起玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "是吗～真可惜……\x01",
            "真想要点提示啊～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "我说，玛丽～，\x01",
            "幸福之石是什么呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14E,
        (
            "#1714F呃，嗯…………\x02\x03",

            "#1713F（……是什么来着。）\x02\x03",

            "（……不知道了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_714")

    label("loc_60D")


    ChrTalk(    #16
        0xFE,
        "咦～，是玛丽。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "波利呢？\x01",
            "你们没在一起吗～？\x02",
        )
    )

    Jump("loc_65B")

    label("loc_65B")

    CloseMessageWindow()

    ChrTalk(    #18
        0x14E,
        (
            "#1713F嗯、嗯……\x02\x03",

            "#1712F波利在和\x01",
            "克拉姆他们一起玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "是吗～真可惜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "你们要再来参观\x01",
            "义卖会哦～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14E,
        (
            "#1710F嗯、嗯。\x01",
            "我会转达他们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_714")

    OP_A2(0x2F3D)

    label("loc_717")

    Jump("loc_E4C")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_809")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_785")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #22
        0xFE,
        "悬崖边上、悬崖边上……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "……………………真是个难题！\x02",
    )

    CloseMessageWindow()
    Jump("loc_806")

    label("loc_785")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #24
        0xFE,
        "悬崖边上、悬崖边上……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x14F, 400)
    Sleep(500)

    ChrTalk(    #25
        0xFE,
        (
            "波利～，\x01",
            "给点提示吧！\x02",
        )
    )

    Jump("loc_802")

    label("loc_802")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_806")

    Jump("loc_B25")

    label("loc_809")


    ChrTalk(    #26
        0x14E,
        (
            "#1710F那个，卢西亚，\x01",
            "你知道幸福之石吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "咦……？\x02",
    )

    Jump("loc_85D")

    label("loc_85D")

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0xFE)

    ChrTalk(    #28
        0xFE,
        "哇啊……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14E,
        "#1714F（哇，好灿烂的笑容……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "……幸福之石？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "什么什么，\x01",
            "快告诉卢西亚～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x14E,
        (
            "#1719F不行不行，\x01",
            "这是秘密啦！\x02\x03",

            "#1711F不过只说一点点\x01",
            "应该也没关系吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "哎呀，告诉我、告诉我啦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x14F,
        (
            "#1731F就是说呢～\x01",
            "被魔兽袭击了呢～\x01",
            "安全绳索断了呢～……\x02\x03",

            "#1732F…………就在悬崖边上～。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1500)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    TurnDirection(0x14E, 0x14F, 500)
    Sleep(500)

    ChrTalk(    #35
        0x14E,
        (
            "#1714F（嗯…………\x01",
            "　这不是欧尼尔叔叔的话吗？）\x02\x03",

            "#1712F（波利这么一说\x01",
            "  听起来像是别的事情似的……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #36
        0xFE,
        "…………悬崖边上？\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x20)

    ChrTalk(    #37
        0xFE,
        "#4S卢·西·亚·大·震·惊！！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x1F4)
    CloseMessageWindow()
    ClearMapFlags(0x20)
    Sleep(200)
    OP_A2(0x2F3C)
    OP_A3(0x1)

    label("loc_B25")

    Jump("loc_E4C")

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 3)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CDA")
    OP_8C(0xFE, 0, 0)
    OP_4A(0x14, 255)

    ChrTalk(    #38
        0xFE,
        "啊，再右边点！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 45, 400)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_B9D")

    ChrTalk(    #39
        0x14,
        "#822F咦？　这、这里吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCC")

    label("loc_B9D")


    NpcTalk(    #40
        0x14,
        "男人",
        "#822F咦？　这、这里吗？\x02",
    )

    Jump("loc_BCB")

    label("loc_BCB")

    CloseMessageWindow()

    label("loc_BCC")


    ChrTalk(    #41
        0xFE,
        "啊～，这次太靠右了～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(    #42
        0x14,
        "#822F嗯嗯…………\x02",
    )

    CloseMessageWindow()
    Jump("loc_C40")

    label("loc_C17")


    NpcTalk(    #43
        0x14,
        "男人",
        "#822F嗯嗯…………\x02",
    )

    Jump("loc_C3F")

    label("loc_C3F")

    CloseMessageWindow()

    label("loc_C40")

    OP_8C(0x14, 0, 400)
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        "啊，太靠左边了。\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(    #45
        0x14,
        "#823F……这么复杂的指示……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD3")

    label("loc_CA0")


    NpcTalk(    #46
        0x14,
        "男人",
        "#823F……这么复杂的指示……\x02",
    )

    Jump("loc_CD2")

    label("loc_CD2")

    CloseMessageWindow()

    label("loc_CD3")

    OP_4B(0x14, 255)
    Jump("loc_D3D")

    label("loc_CDA")


    ChrTalk(    #47
        0xFE,
        (
            "卢西亚不懂，\x01",
            "还是拜托游击士大哥哥吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "……大哥哥的名字，\x01",
            "叫什么来着～？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D3D")

    Jump("loc_E42")

    label("loc_D40")


    ChrTalk(    #49
        0xFE,
        "啊，你们来了啊～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14F,
        "#1732F因为好像很有趣嘛～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "嗯，一定很有趣的★\x01",
            "卢西亚给你们打包票！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x14E,
        (
            "#1710F我说，卢西亚。\x01",
            "义卖会在哪里开啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "那个啊，是在风车小屋开的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "你们俩都要来\x01",
            "尽情买东西哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3B)

    label("loc_E42")

    Jump("loc_E4C")

    label("loc_E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_E4C")

    label("loc_E4C")

    TalkEnd(0xFE)
    Return()

    # Function_2_2AB end

    def Function_3_E50(): pass

    label("Function_3_E50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1164")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 0)), scpexpr(EXPR_END)), "loc_F07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA9")

    ChrTalk(    #55
        0x14,
        (
            "#820F有什么麻烦的话，\x01",
            "随时都可以跟我说哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F04")

    label("loc_EA9")


    ChrTalk(    #56
        0x14,
        (
            "#820F别看我这样，我也是游击士呢。\x02\x03",

            "有什么麻烦的话，\x01",
            "别客气只管说哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F04")

    Jump("loc_FDD")

    label("loc_F07")


    ChrTalk(    #57
        0x14,
        (
            "#821F欢迎，欢迎！\x01",
            "……这不是刚才的孩子吗。\x02\x03",

            "#820F怎么了？\x01",
            "发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14E,
        (
            "#1713F嗯、嗯，\x01",
            "没什么……\x02\x03",

            "#1712F（波利瞎晃悠\x01",
            "  是常有的事啦。）\x02\x03",

            "（反正很快就会找到的！）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F40)

    label("loc_FDD")

    Jump("loc_1161")

    label("loc_FE0")

    OP_8C(0x14, 90, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #59
        0x14,
        "男人",
        "嗯……怎么了？\x02",
    )

    Jump("loc_1049")

    label("loc_1049")

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #60
        0x14E,
        (
            "#1714F啊…………想起来了。\x02\x03",

            "嗯………………\x01",
            "……是叫……\x01",
            "………布莱克先生……？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    NpcTalk(    #61
        0x14,
        "男人",
        "你的记忆还真混乱啊……\x02",
    )

    Jump("loc_1124")

    label("loc_1124")

    CloseMessageWindow()

    ChrTalk(    #62
        0x14,
        (
            "#823F……是库拉茨。\x01",
            "各位，要记住我的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_1161")

    Jump("loc_2116")

    label("loc_1164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_18C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 7)), scpexpr(EXPR_END)), "loc_13E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_12F4")
    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11D8")

    ChrTalk(    #63
        0x13,
        "可是，是在悬崖边上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x14,
        "#823F（完全莫名其妙……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_11D8")


    ChrTalk(    #65
        0x13,
        (
            "那个，\x01",
            "叫做幸福之石的，\x01",
            "就是玛丽和波利提到过的东西吧？\x02",
        )
    )

    Jump("loc_1223")

    label("loc_1223")

    CloseMessageWindow()

    ChrTalk(    #66
        0x14,
        (
            "#825F啊～\x01",
            "那个就别管啦……\x02\x03",

            "这个传单，\x01",
            "就贴在这里可以吗？\x02",
        )
    )

    Jump("loc_1276")

    label("loc_1276")

    CloseMessageWindow()

    ChrTalk(    #67
        0x13,
        (
            "那个啊，一定是亮晶晶的，\x01",
            "这种感觉吧～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x14,
        (
            "#825F（…………女孩子啊，\x01",
            "　还真喜欢这方面的事呢～。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12F1")

    Jump("loc_13E5")

    label("loc_12F4")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1352")

    ChrTalk(    #69
        0x14,
        (
            "#820F虽然对工作热心是很好……\x01",
            "但真是不想让这种类型的人当上司呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E5")

    label("loc_1352")


    ChrTalk(    #70
        0x14,
        (
            "#820F我想放在这边\x01",
            "应该差不多了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x13,
        (
            "不行！\x01",
            "这叫做半途而废！\x02",
        )
    )

    Jump("loc_13AD")

    label("loc_13AD")

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        "#825F……唉，真是让人伤脑筋的主人啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_13E5")

    Jump("loc_18C5")

    label("loc_13E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x140, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_154C")

    ChrTalk(    #73
        0x14,
        "#821F啊…………\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #74
        (
            "\x07\x05库拉茨好像在看\x01",
            "玛丽拿着的土人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #75
        0x14,
        (
            "#823F不、不，\x01",
            "没什么……\x02\x03",

            "（那个道具，\x01",
            "  是我拿来卖的……）\x02\x03",

            "#825F（其实是很贵重的东西……\x01",
            "  ……不过算了。）\x02\x03",

            "#821F要好好珍藏哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14E,
        "#1714F是、是的…………？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_18C5")

    label("loc_154C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x139, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_164B")

    ChrTalk(    #77
        0x14,
        "#821F啊…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    OP_63(0x14F)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #78
        (
            "\x07\x05库拉茨好像在看\x01",
            "波利戴的柔软编织帽。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #79
        0x14,
        (
            "#823F不、不，\x01",
            "没什么……\x02\x03",

            "#825F（那顶帽子，\x01",
            "  是我拿来卖的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_18C5")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_17CE")
    OP_8C(0x14, 0, 0)
    OP_4A(0x13, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16AE")

    ChrTalk(    #80
        0x13,
        "可是，是在悬崖边上！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14,
        "#823F（完全莫名其妙……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_17CB")

    label("loc_16AE")


    ChrTalk(    #82
        0x13,
        (
            "那个，\x01",
            "叫做幸福之石的，\x01",
            "就是玛丽和波利提到过的东西吧？\x02",
        )
    )

    Jump("loc_16F9")

    label("loc_16F9")

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        (
            "#825F啊～\x01",
            "那个就别管啦……\x02\x03",

            "这个传单，\x01",
            "就贴在这里可以吗？\x02",
        )
    )

    Jump("loc_174C")

    label("loc_174C")

    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "那个啊，一定是亮晶晶的，\x01",
            "这种感觉吧～㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x14,
        (
            "#823F（…………女孩子啊，\x01",
            "　还真喜欢这方面的事呢～。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_A2(0x1)

    label("loc_17CB")

    Jump("loc_18C5")

    label("loc_17CE")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_182A")

    ChrTalk(    #86
        0x14,
        (
            "#825F虽然对工作热心很好……\x01",
            "但真是不想让这种类型的人当上司呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C5")

    label("loc_182A")

    OP_4A(0x13, 255)

    ChrTalk(    #87
        0x14,
        (
            "#820F我想放在这边\x01",
            "应该差不多了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x13,
        (
            "不行！\x01",
            "这叫做半途而废！\x02",
        )
    )

    Jump("loc_1889")

    label("loc_1889")

    CloseMessageWindow()

    ChrTalk(    #89
        0x14,
        "#825F……唉，真是让人伤脑筋的主人啊……\x02",
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_A2(0x1)

    label("loc_18C5")

    Jump("loc_1DF5")

    label("loc_18C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 7)), scpexpr(EXPR_END)), "loc_1A05")
    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #90
        0x14,
        "男人",
        "嗯……怎么了？\x02",
    )

    Jump("loc_1938")

    label("loc_1938")

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #91
        0x14E,
        (
            "#1714F啊……想起来了！！\x02\x03",

            "#1711F是布莱克先生！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #92
        0x14,
        (
            "#823F……是库拉茨。\x01",
            "各位，要记住我的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)
    Jump("loc_1DF5")

    label("loc_1A05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x140, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BA2")

    NpcTalk(    #93
        0x14,
        "男人",
        "啊…………\x02",
    )

    Jump("loc_1A35")

    label("loc_1A35")

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x07\x05男人好像在看\x01",
            "玛丽拿着的土人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #95
        0x14,
        "男人",
        (
            "不、不，\x01",
            "没什么……\x02",
        )
    )

    Jump("loc_1AD2")

    label("loc_1AD2")

    CloseMessageWindow()

    NpcTalk(    #96
        0x14,
        "男人",
        (
            "（那个道具，\x01",
            "  是我拿来卖的……）\x02",
        )
    )

    Jump("loc_1B0B")

    label("loc_1B0B")

    CloseMessageWindow()

    NpcTalk(    #97
        0x14,
        "男人",
        (
            "（其实是很贵重的东西……\x01",
            "  ……不过算了。）\x02",
        )
    )

    Jump("loc_1B4E")

    label("loc_1B4E")

    CloseMessageWindow()

    NpcTalk(    #98
        0x14,
        "男人",
        "要好好珍藏哦！\x02",
    )

    Jump("loc_1B74")

    label("loc_1B74")

    CloseMessageWindow()

    ChrTalk(    #99
        0x14E,
        "#1714F是、是的…………？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_1DF5")

    label("loc_1BA2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x139, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CC8")

    NpcTalk(    #100
        0x14,
        "男人",
        "啊…………\x02",
    )

    Jump("loc_1BD2")

    label("loc_1BD2")

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    OP_63(0x14F)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x05库拉茨好像在看\x01",
            "波利戴的柔软编织帽。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #102
        0x14,
        "男人",
        (
            "不、不，\x01",
            "没什么……\x02",
        )
    )

    Jump("loc_1C88")

    label("loc_1C88")

    CloseMessageWindow()

    NpcTalk(    #103
        0x14,
        "男人",
        (
            "（那顶帽子，\x01",
            "  是我拿来卖的……）\x02",
        )
    )

    Jump("loc_1CC1")

    label("loc_1CC1")

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_1DF5")

    label("loc_1CC8")

    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #104
        0x14,
        "男人",
        "嗯……怎么了？\x02",
    )

    Jump("loc_1D31")

    label("loc_1D31")

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #105
        0x14E,
        (
            "#1711F啊……想起来了！！\x02\x03",

            "是布莱克先生！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #106
        0x14,
        (
            "#823F……是库拉茨。\x01",
            "各位，要记住我的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_1DF5")

    Jump("loc_2116")

    label("loc_1DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 3)), scpexpr(EXPR_END)), "loc_1EB4")
    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E46")

    ChrTalk(    #107
        0x14,
        "#820F贴在这里就可以了吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB1")

    label("loc_1E46")


    ChrTalk(    #108
        0x14,
        (
            "#822F……唔～\x01",
            "贴得太高的话很难看到吧。\x02\x03",

            "#821F这里有不少老人和孩子，\x01",
            "还是贴低一点吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1EB1")

    Jump("loc_1FD6")

    label("loc_1EB4")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F37")

    ChrTalk(    #109
        0x14,
        (
            "#823F虽然我是柏斯支部所属的，\x01",
            "最近却一直在\x01",
            "卢安工作啊～……\x02\x03",

            "唉，\x01",
            "都快一个月没回去了……\x02",
        )
    )

    Jump("loc_1F33")

    label("loc_1F33")

    CloseMessageWindow()
    Jump("loc_1FD6")

    label("loc_1F37")


    ChrTalk(    #110
        0x14,
        (
            "#823F嘉恩那家伙，\x01",
            "硬把工作都塞给我……\x02\x03",

            "帮忙义卖会这种事，\x01",
            "根本就不适合我嘛。\x02\x03",

            "#824F这应该是卡露娜的工作吧？\x01",
            "那个家伙，给我记住！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1FD6")

    Jump("loc_210C")

    label("loc_1FD9")

    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #111
        0x14,
        "男人",
        "嗯……怎么了？\x02",
    )

    Jump("loc_2042")

    label("loc_2042")

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #112
        0x14E,
        (
            "#1714F啊……想起来了！！\x02\x03",

            "#1711F是布莱克先生！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #113
        0x14,
        (
            "#823F……是库拉茨。\x01",
            "各位，要记住我的名字哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_210C")

    Jump("loc_2116")

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_2116")

    label("loc_2116")

    TalkEnd(0xFE)
    Return()

    # Function_3_E50 end

    def Function_4_211A(): pass

    label("Function_4_211A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_2127")
    Jump("loc_2364")

    label("loc_2127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2187")

    ChrTalk(    #114
        0xFE,
        "……一定是这个村子的人吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "因为他正那么开心地\x01",
            "在给义卖会帮忙嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_2187")


    ChrTalk(    #116
        0xFE,
        (
            "……和卢西亚在一起的\x01",
            "那个男人是谁啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "感觉好像以前见过似的，\x01",
            "是玛诺利亚村的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_21EA")

    Jump("loc_2364")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_229B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_224E")

    ChrTalk(    #118
        0xFE,
        (
            "如果是花的话，\x01",
            "应该会有人买的。\x02\x03",

            "因为一看到漂亮的花\x01",
            "就会感到放松对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2298")

    label("loc_224E")


    ChrTalk(    #119
        0xFE,
        "……差不多到中午了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "嗯，得把店收起来\x01",
            "去参加义卖会了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2298")

    Jump("loc_2364")

    label("loc_229B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_235D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22E2")

    ChrTalk(    #121
        0xFE,
        "怎么还没到中午呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "感觉心里老不踏实啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_235A")

    label("loc_22E2")


    ChrTalk(    #123
        0xFE,
        "今天义卖会就要开始了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "我也打算从下午开始\x01",
            "去那里帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "呵呵，\x01",
            "我也拿一些盆栽去卖吧。\x02",
        )
    )

    Jump("loc_2356")

    label("loc_2356")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_235A")

    Jump("loc_2364")

    label("loc_235D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_2364")

    label("loc_2364")

    TalkEnd(0xFE)
    Return()

    # Function_4_211A end

    def Function_5_2368(): pass

    label("Function_5_2368")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-1560, 6000, -3200, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(328000, 0)
    OP_6E(340, 0)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    SetChrPos(0x14E, 3300, 6500, -2840, 90)
    SetChrPos(0x14F, 3300, 6500, -2840, 90)

    def lambda_23E3():
        OP_6D(5100, 6000, 960, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_23E3)

    def lambda_23FB():
        OP_67(0, 6360, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_23FB)

    def lambda_2413():
        OP_6B(2440, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2413)

    def lambda_2423():
        OP_6C(318000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2423)

    def lambda_2433():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2433)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x1C2, 0x0, 0x64)
    OP_0D()
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    Sleep(200)
    OP_43(0x14E, 0x2, 0x0, 0x6)
    OP_43(0x14F, 0x2, 0x0, 0x7)
    Sleep(2500)
    OP_72(0x2, 0x8)
    ExitThread()
    OP_6F(0x2, 29)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x2, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x1C2)
    WaitChrThread(0x14E, 0x2)
    WaitChrThread(0x14F, 0x2)

    ChrTalk(    #126
        0x14E,
        "#1719F呼……\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    OP_8C(0x14E, 180, 500)
    Sleep(400)

    ChrTalk(    #127
        0x14E,
        (
            "#1718F怎、怎么办啊波利！\x01",
            "听到了不得了的话……！\x02\x03",

            "高山果然还是有\x01",
            "不可思议的力量的……\x02\x03",

            "#1903F这、这是真事啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14F,
        "#1730F我说，玛丽……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(400)

    ChrTalk(    #129
        0x14E,
        (
            "#1719F（说、说不定古罗尼山峰\x01",
            "  真的有幸福之石……）\x02\x03",

            "#1711F（那、那样的话\x01",
            "  就说得通了对吧……？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x14F,
        (
            "#1733F……玛丽，\x01",
            "你都不听我说话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x14E,
        (
            "#1719F……………………\x02\x03",

            "就、就过去\x01",
            "看一下吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 400)
    Sleep(400)

    ChrTalk(    #132
        0x14E,
        "#1718F我说，波利……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x14F,
        (
            "#1731F……玛丽，刚才啊～\x01",
            "克拉姆和达尼艾尔\x01",
            "来过了哦～？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(200)

    ChrTalk(    #134
        0x14E,
        "#1714F#3S……咦！？#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #135
        0x14F,
        (
            "#1730F说要去古罗尼山道～\x01",
            "还买了很多东西～……\x02\x03",

            "说什么准备完全了呢～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x14E,
        (
            "#1714F那是真的吗！？\x01",
            "我完全没注意到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14F,
        (
            "#1731F玛丽最近\x01",
            "总是在发呆呢～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x14E,
        (
            "#1715F克、克拉姆真是的！\x02\x03",

            "老师不是一直说\x01",
            "不能跑到比玛诺利亚村更远的地方嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x14F,
        (
            "#1733F玛丽不是也打算\x01",
            "去古罗尼山道吗～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x14E,
        (
            "#1900F（吓一跳）……\x02\x03",

            "#1903F因、因为要寻找\x01",
            "老师的生日礼物…………\x01",
            "就去一下没关系啦！\x02\x03",

            "而、而且还要把那两人\x01",
            "带回来才行啊。\x01",
            "这个只是顺便……对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x14F,
        (
            "#1731F……………………\x02\x03",

            "#1730F对老师要保密吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x14E,
        (
            "#1710F对，一定要保密哦。\x01",
            "因为是她的生日嘛！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29B5():
        OP_8E(0xFE, 0x15CC, 0x1770, 0x104, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_29B5)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #143
        0x14E,
        (
            "#1718F#11P……好，走吧！\x01",
            "波利，别走散哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 400)
    Sleep(600)

    def lambda_2A17():
        OP_8E(0xFE, 0x15CC, 0x1770, 0x2044, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2A17)

    def lambda_2A32():
        OP_8E(0xFE, 0x1644, 0x1770, 0x1D9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2A32)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x14E, 0x1)
    OP_44(0x14F, 0x2)
    SetChrPos(0x14E, 4120, 4000, 15700, 0)
    SetChrPos(0x14F, 4120, 4000, 15700, 0)
    ClearChrFlags(0x14E, 0x40)
    OP_71(0x2, 0x8)
    ExitThread()
    OP_6F(0x2, 0)
    OP_A2(0x2F21)
    EventEnd(0x0)
    FadeToBright(1000, 0)
    Return()

    # Function_5_2368 end

    def Function_6_2AA2(): pass

    label("Function_6_2AA2")


    def lambda_2AA8():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFF5D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2AA8)
    WaitChrThread(0x14E, 0x1)

    def lambda_2AC8():
        OP_8E(0xFE, 0x1644, 0x1770, 0x49C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_2AC8)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_6_2AA2 end

    def Function_7_2AE3(): pass

    label("Function_7_2AE3")

    Sleep(1200)

    def lambda_2AEE():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFF5D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2AEE)
    WaitChrThread(0x14F, 0x1)

    def lambda_2B0E():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFFE5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_2B0E)
    WaitChrThread(0x14F, 0x1)
    Return()

    # Function_7_2AE3 end

    def Function_8_2B29(): pass

    label("Function_8_2B29")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #144
        (
            "\x07\x05　　　●第３回玛诺利亚村义卖会正在进行！●\x01\x01",
            "今年玛诺利亚村义卖会的季节又到来了。\x01",
            "从本日开始的３天，将在风车小屋举行。\x01",
            "家中不需要的物品，或者还能使用的旧东西，\x01",
            "请务必拿出来作为商品出售。\x01",
            "说不定会意外淘到好东西。\x01",
            "各位，请积极参与！\x01\x01",
            "　　　　　　　　　　玛诺利亚村义卖会实行委员会\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2B29 end

    def Function_9_2C73(): pass

    label("Function_9_2C73")

    SetPlaceName(0x58)
    Return()

    # Function_9_2C73 end

    def Function_10_2C77(): pass

    label("Function_10_2C77")

    SetPlaceName(0x57)
    Return()

    # Function_10_2C77 end

    def Function_11_2C7B(): pass

    label("Function_11_2C7B")

    SetPlaceName(0x59)
    Return()

    # Function_11_2C7B end

    SaveToFile()

Try(main)
