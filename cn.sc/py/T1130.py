from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1130   ._SN',
        MapName             = 'Bose',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 1,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1130_1 ._SN',
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
        '豪尔斯教区长',                         # 9
        '修女萝萨',                             # 10
        '哈尔德',                               # 11
        '丽露露',                               # 12
        '格蕾娅',                               # 13
        '科尔娜',                               # 14
        '雅哈多老人',                           # 15
        '萨拉',                                 # 16
        '莉拉',                                 # 17
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01350 ._CH',             # 07
        'ED6_DT07/CH02370 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01350P._CP',             # 07
        'ED6_DT07/CH02370P._CP',             # 08
    )

    DeclNpc(
        X                   = 59100,
        Z                   = 1000,
        Y                   = 52100,
        Direction           = 180,
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
        X                   = 63070,
        Z                   = 0,
        Y                   = 48320,
        Direction           = 180,
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
        X                   = 56670,
        Z                   = 0,
        Y                   = 43550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 60350,
        Z                   = 0,
        Y                   = 45170,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 58930,
        Z                   = 0,
        Y                   = 44670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = 46900,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 58180,
        Z                   = 0,
        Y                   = 45750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 61740,
        Z                   = 0,
        Y                   = 46550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 57200,
        Z                   = 0,
        Y                   = 47070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50250,
        TriggerRange        = 400,
        ActorX              = 59100,
        ActorZ              = 2500,
        ActorY              = 52100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16410,
        TriggerZ            = 4000,
        TriggerY            = 43010,
        TriggerRange        = 800,
        ActorX              = 16410,
        ActorZ              = 5200,
        ActorY              = 43010,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_2F1",          # 01, 1
        "Function_2_344",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_AFF",          # 04, 4
        "Function_5_FDE",          # 05, 5
        "Function_6_10E3",         # 06, 6
        "Function_7_1143",         # 07, 7
        "Function_8_12BB",         # 08, 8
        "Function_9_130B",         # 09, 9
        "Function_10_142F",        # 0A, 10
        "Function_11_14F9",        # 0B, 11
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_269")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_2F0")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_278")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_2F0")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_282")
    Jump("loc_2F0")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_291")
    SetChrFlags(0x9, 0x80)
    Jump("loc_2F0")

    label("loc_291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2A5")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_2F0")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2DD")
    OP_64(0x0, 0x1)
    SetChrPos(0x8, 59100, 0, 48100, 180)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_2F0")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x9, 0xA, 0)

    label("loc_2F0")

    Return()

    # Function_0_25A end

    def Function_1_2F1(): pass

    label("Function_1_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_303")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)

    label("loc_303")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E")
    OP_65(0x1, 0x1)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_343")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_343")
    OP_64(0x0, 0x1)

    label("loc_343")

    Return()

    # Function_1_2F1 end

    def Function_2_344(): pass

    label("Function_2_344")

    Call(0, 3)
    Return()

    # Function_2_344 end

    def Function_3_349(): pass

    label("Function_3_349")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_434")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA")

    ChrTalk(    #0
        0x8,
        (
            "人们的脸上稍微\x01",
            "有了点光彩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "行走在道路上的人们，脚步\x01",
            "也轻快了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "嗯嗯，这是个好兆头。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "状态恢复的快，\x01",
            "这正是这柏斯市的长处所在啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_431")

    label("loc_3FA")


    ChrTalk(    #4
        0x8,
        (
            "人们的脸上稍微\x01",
            "有了点光彩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "嗯，是个好兆头。\x02",
    )

    CloseMessageWindow()

    label("loc_431")

    Jump("loc_AFB")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")

    ChrTalk(    #6
        0x8,
        (
            "哎呀哎呀，\x01",
            "昨天晚上那是场很严重的骚乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "情绪激动的市民们\x01",
            "包围了协会和市长官邸，\x01",
            "吵闹了整整一个晚上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "虽然梅贝尔小姐的劝说取得了效果，\x01",
            "事态在变得严重前得到了控制……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "但导力器所带来的影响\x01",
            "需要我们重新认识一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_590")

    label("loc_530")


    ChrTalk(    #10
        0x8,
        (
            "哎呀哎呀，\x01",
            "昨天晚上那是场很严重的骚乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "但导力器所带来的影响\x01",
            "需要我们重新认识一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590")

    Jump("loc_AFB")

    label("loc_593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5EE")

    ChrTalk(    #12
        0x8,
        (
            "柏斯一带终于\x01",
            "恢复了平静啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "拉文努村的果树园也\x01",
            "有了复苏的迹象。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B6")

    label("loc_5EE")


    ChrTalk(    #14
        0x8,
        (
            "柏斯一带终于\x01",
            "恢复了平静啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "超市顺利恢复营业，\x01",
            "拉文努村的果树园\x01",
            "也有了复苏的迹象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "复兴虽然需要时间，\x01",
            "但是，一定能够实现的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "毕竟柏斯市是从那场战争中\x01",
            "奇迹般的迅速恢复过来的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6B6")

    Jump("loc_AFB")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_80F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_75B")

    ChrTalk(    #18
        0x8,
        (
            "梅贝尔市长\x01",
            "相当努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "但几乎不顾自己的身体这点\x01",
            "让我有点担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "人在年轻的时候谁都是这样的吧。\x01",
            "我年轻的时候也是这么不顾一切的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80C")

    label("loc_75B")


    ChrTalk(    #21
        0x8,
        (
            "梅贝尔市长\x01",
            "相当努力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "可以说她工作的风采已经不输给\x01",
            "身为前市长的父亲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "但几乎不顾自己的身体这点\x01",
            "让我有点担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "呵呵，人在年轻的时候\x01",
            "谁都是这样的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_80C")

    Jump("loc_AFB")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_876")

    ChrTalk(    #25
        0x8,
        (
            "市长官邸的女佣\x01",
            "好像还没有恢复意识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "我已经把我所知道的\x01",
            "药的处方都用过了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903")

    label("loc_876")


    ChrTalk(    #27
        0x8,
        (
            "很遗憾，\x01",
            "市长官邸的女佣\x01",
            "好像还没有恢复意识。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "我已经把我所知道的\x01",
            "药的处方都用过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "剩下的就只有等待\x01",
            "看护修女的好消息了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_903")

    Jump("loc_AFB")

    label("loc_906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_9A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_954")

    ChrTalk(    #30
        0x8,
        "请大家冷静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "直到王国军赶来前，\x01",
            "女神会保佑我们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A5")

    label("loc_954")


    ChrTalk(    #32
        0x8,
        "请大家冷静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "很快\x01",
            "王国军就会赶到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "在这之前女神会\x01",
            "保佑大家的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9A5")

    Jump("loc_AFB")

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_AFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2E")

    ChrTalk(    #35
        0x8,
        (
            "多亏了超市，\x01",
            "只要得到许可，谁都可以开一家\x01",
            "在市场里的商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "呵呵，也难怪这些初出茅庐\x01",
            "的商人们会聚集在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFB")

    label("loc_A2E")


    ChrTalk(    #37
        0x8,
        (
            "作为商人之城的柏斯市，\x01",
            "一直以来就对商业有所保护。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "位于市中心的超市\x01",
            "可以说是其象征吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "总之只要得到许可的话，\x01",
            "就可以在里面开一家店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "呵呵，也难怪这些初出茅庐\x01",
            "的商人们会聚集在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AFB")

    TalkEnd(0x8)
    Return()

    # Function_3_349 end

    def Function_4_AFF(): pass

    label("Function_4_AFF")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_C7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF4")

    ChrTalk(    #41
        0xFE,
        (
            "超市已经完全恢复\x01",
            "到以前的样子了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "一靠近，\x01",
            "就听到很有气势的叫卖声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "必定是梅贝尔市长的视察\x01",
            "把超市的能量都发挥出来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "呵呵，这是理所当然的事情吧。\x01",
            "本来计划要去教堂做礼拜的，\x01",
            "却偏偏临时说有事要办。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C7A")

    label("loc_BF4")


    ChrTalk(    #45
        0xFE,
        (
            "而且还常在礼拜做到一半的时候跑掉，\x01",
            "这种态度的确有点难以容忍呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "我觉得身为市长，\x01",
            "不可以在市民面前做出这种不虔诚的举止啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A")

    Jump("loc_FDA")

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6A")

    ChrTalk(    #47
        0xFE,
        (
            "没想到只是因为导力器无法使用\x01",
            "就造成了这样的混乱……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "作为信奉女神的人来说\x01",
            "真是件羞耻的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "正是因为过于依赖导力器\x01",
            "才会导致这种事情发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "真希望人们可以通过这次女神给予的启示和教训，\x01",
            "从中觉醒过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_DDE")

    label("loc_D6A")


    ChrTalk(    #51
        0xFE,
        (
            "正是因为过于依赖导力器\x01",
            "才会导致这种事情发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "真希望人们可以通过这次女神给予的启示和教训，\x01",
            "从中觉醒过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDE")

    Jump("loc_FDA")

    label("loc_DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E5C")

    ChrTalk(    #53
        0xFE,
        (
            "今天起超市将恢复营业，\x01",
            "这样一来柏斯也将恢复原貌了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "购物的乐趣\x01",
            "只有在和平的时候才体会得到呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F15")

    label("loc_E5C")


    ChrTalk(    #55
        0xFE,
        (
            "今天起超市将恢复营业，\x01",
            "这样一来柏斯也将恢复原貌了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "来教堂做礼拜的人\x01",
            "总感觉还是很少的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "购物的乐趣\x01",
            "只有在和平的时候才体会得到呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "今天一天\x01",
            "不打算计较了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F15")

    Jump("loc_FDA")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F79")

    ChrTalk(    #59
        0xFE,
        (
            "有很多祈求生意兴隆的\x01",
            "人来教堂礼拜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "啊，面对创造女神\x01",
            "就不觉得失礼吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDA")

    label("loc_F79")


    ChrTalk(    #61
        0xFE,
        "在那边祈祷的几位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "好像是来\x01",
            "祈求生意兴隆的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "为这种俗事祈祷，\x01",
            "不觉得失礼吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FDA")

    TalkEnd(0x9)
    Return()

    # Function_4_AFF end

    def Function_5_FDE(): pass

    label("Function_5_FDE")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_10DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(    #64
        0xFE,
        (
            "我是为商业洽谈的\x01",
            "成功来祈祷的……\x02\x03",

            "从刚才起修女就\x01",
            "一直盯着这边看。\x02\x03",

            "是我干了什么坏事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DF")

    label("loc_1050")


    ChrTalk(    #65
        0xFE,
        (
            "我将要去超市\x01",
            "开门营业。\x02\x03",

            "为了祈求商业洽谈成功，\x01",
            "就来这里祈祷了。\x02\x03",

            "不过，从刚才起修女就\x01",
            "一直盯着这里看……\x02\x03",

            "怎么回事？\x01",
            "我并没做坏事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_10DF")

    TalkEnd(0xA)
    Return()

    # Function_5_FDE end

    def Function_6_10E3(): pass

    label("Function_6_10E3")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_113F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1101")

    ChrTalk(    #66
        0xFE,
        "呜～\x02",
    )

    CloseMessageWindow()
    Jump("loc_113F")

    label("loc_1101")


    ChrTalk(    #67
        0xFE,
        (
            "超市里\x01",
            "一下子暗了下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "使我好害怕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "呜～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_113F")

    TalkEnd(0xB)
    Return()

    # Function_6_10E3 end

    def Function_7_1143(): pass

    label("Function_7_1143")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C2")

    ChrTalk(    #70
        0xFE,
        (
            "很久没有来\x01",
            "向女神祈祷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "因为超市那边\x01",
            "实在脱不开身……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "现在去买东西\x01",
            "一点乐趣都没有……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_11FD")

    label("loc_11C2")


    ChrTalk(    #73
        0xFE,
        (
            "很久没有来\x01",
            "向女神祈祷了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "不能把心静下来的话……\x02",
    )

    CloseMessageWindow()

    label("loc_11FD")

    Jump("loc_12B7")

    label("loc_1200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_12B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_124E")

    ChrTalk(    #75
        0xFE,
        (
            "袭击超市的好像是\x01",
            "巨大的怪物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "真是件可怕的事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12B7")

    label("loc_124E")


    ChrTalk(    #77
        0xFE,
        (
            "袭击超市的好像是\x01",
            "巨大的怪物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "而且那头怪物现在\x01",
            "还正在某处飞着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "真是件可怕的事……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_12B7")

    TalkEnd(0xC)
    Return()

    # Function_7_1143 end

    def Function_8_12BB(): pass

    label("Function_8_12BB")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1307")

    ChrTalk(    #80
        0xFE,
        (
            "超市被那么巨大的\x01",
            "怪物袭击……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "啊啊，但愿\x01",
            "那个女孩没事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1307")

    TalkEnd(0xD)
    Return()

    # Function_8_12BB end

    def Function_9_130B(): pass

    label("Function_9_130B")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_142B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_137B")

    ChrTalk(    #82
        0xFE,
        (
            "话虽如此……\x01",
            "那到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "就好像是\x01",
            "传说中的龙一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "……真不敢相信啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_142B")

    label("loc_137B")


    ChrTalk(    #85
        0xFE,
        "那怪物是从东面飞过来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "开始还只是隐约可见呢，\x01",
            "但一下子就飞到超市上空了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "然后就刮起了强风。\x01",
            "我都以为自己要被吹走了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "呼，但愿市长\x01",
            "的下属没事就好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_142B")

    TalkEnd(0xE)
    Return()

    # Function_9_130B end

    def Function_10_142F(): pass

    label("Function_10_142F")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_14F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #89
        0xFE,
        (
            "我出来买东西，\x01",
            "顺便就过来做祷告了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "祈祷莉拉能\x01",
            "早日醒来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F5")

    label("loc_1487")


    ChrTalk(    #91
        0xFE,
        (
            "我出来买东西，\x01",
            "顺便就过来做祷告了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "祈祷莉拉能\x01",
            "早日醒来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "啊，希望女神能够\x01",
            "倾听我的祈求……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_14F5")

    TalkEnd(0xF)
    Return()

    # Function_10_142F end

    def Function_11_14F9(): pass

    label("Function_11_14F9")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B7")

    ChrTalk(    #94
        0x10,
        (
            "#620F梅贝尔小姐\x01",
            "正在视察超市。\x02\x03",

            "也就是说\x01",
            "这次祈祷她又偷懒了。\x02\x03",

            "因为现在这种情况，\x01",
            "我就先不说了……\x02\x03",

            "等城里所有的事情都安定下来之后，\x01",
            "一定要让小姐老老实实地做祈祷才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_15FA")

    label("loc_15B7")


    ChrTalk(    #95
        0x10,
        (
            "#620F梅贝尔小姐\x01",
            "正在视察超市。\x02\x03",

            "也就是说\x01",
            "这次祈祷她又偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FA")

    TalkEnd(0x10)
    Return()

    # Function_11_14F9 end

    SaveToFile()

Try(main)
