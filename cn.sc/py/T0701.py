from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0701   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0701.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0701_1 ._SN',
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
        '赛希莉亚号',                           # 9
        '法布利',                               # 10
        '斯库拉特',                             # 11
        '索斯摩夫',                             # 12
        '洛连特市街区',                         # 13
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 43100,
        Z                   = 4000,
        Y                   = 31800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 38670,
        Z                   = 0,
        Y                   = 50200,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 28880,
        Z                   = 0,
        Y                   = 3000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 35320,
        Z                   = 0,
        Y                   = -13920,
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


    DeclEvent(
        X                   = 37790,
        Y                   = 3000,
        Z                   = 40490,
        Range               = 36410,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x92D6,
        Unknown_18          = 0x10000,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 38000,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = 38000,
        ActorZ              = 2200,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 4000,
        TriggerY            = 41300,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 5500,
        ActorY              = 41800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 34500,
        TriggerZ            = 0,
        TriggerY            = 46570,
        TriggerRange        = 800,
        ActorX              = 35000,
        ActorZ              = 1500,
        ActorY              = 46570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_21B",          # 01, 1
        "Function_2_26C",          # 02, 2
        "Function_3_282",          # 03, 3
        "Function_4_542",          # 04, 4
        "Function_5_7C1",          # 05, 5
        "Function_6_87F",          # 06, 6
        "Function_7_91B",          # 07, 7
        "Function_8_996",          # 08, 8
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    SetChrPos(0x9, 43080, 4000, 32060, 270)

    label("loc_20A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)

    label("loc_21A")

    Return()

    # Function_0_1E6 end

    def Function_1_21B(): pass

    label("Function_1_21B")

    OP_16(0x2, 0xFA0, 0xFFFE98A0, 0xFFFE8518, 0x230007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_245")
    OP_71(0xA, 0x4)

    label("loc_245")

    OP_72(0xB, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xFDE8, 0x0)

    label("loc_26B")

    Return()

    # Function_1_21B end

    def Function_2_26C(): pass

    label("Function_2_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_281")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_26C")

    label("loc_281")

    Return()

    # Function_2_26C end

    def Function_3_282(): pass

    label("Function_3_282")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E0")

    ChrTalk(    #0
        0xFE,
        (
            "哟，游击士们。\x01",
            "刚才辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "总之也发生了不少事……\x01",
            "请注意保密。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_2E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_336")

    ChrTalk(    #2
        0xFE,
        (
            "请赶快\x01",
            "调查船的里面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我可是做好了被炒的准备\x01",
            "在帮助你们哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_348")
    Call(1, 3)
    Jump("loc_539")

    label("loc_348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_3B4")

    ChrTalk(    #4
        0xFE,
        "你们在找索斯摩夫先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "唔～应该\x01",
            "还在飞船坪吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "总之你们别灰心，\x01",
            "去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_3B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_449")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_412")

    ChrTalk(    #7
        0xFE,
        "哟，猫找到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "真是的，你们还要为了这种\x01",
            "委托忙到这么晚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_446")

    label("loc_412")


    ChrTalk(    #9
        0xFE,
        (
            "嗯？你们在找\x01",
            "库因特吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "那家伙\x01",
            "去吃饭了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446")

    Jump("loc_539")

    label("loc_449")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_4A7")

    ChrTalk(    #11
        0xFE,
        (
            "说看到了猫的人\x01",
            "肯定是斯库拉特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "你们去找他问问吧。\x01",
            "他应该在仓库附近。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_539")

    label("loc_4A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4B8")
    Call(1, 0)
    Jump("loc_539")

    label("loc_4B8")


    ChrTalk(    #13
        0xFE,
        (
            "虽然明知有可能没用，\x01",
            "不过我还是在重新做检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "让乘客等着，\x01",
            "自己闲着可不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "不过这雾还真厉害。\x01",
            "连工作服也湿透了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_539")

    TalkEnd(0x9)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_3_282 end

    def Function_4_542(): pass

    label("Function_4_542")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5C1")

    ChrTalk(    #16
        0xFE,
        (
            "哟，游击士们。\x01",
            "听说你们找到猫了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "法布利那家伙\x01",
            "可松了一大口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "虽然我不知道\x01",
            "他有什么好放心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD")

    label("loc_5C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_60A")

    ChrTalk(    #19
        0xFE,
        "哟，这么晚真是辛苦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "怎么样？\x01",
            "猫找到了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD")

    label("loc_60A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_670")

    ChrTalk(    #21
        0xFE,
        (
            "如果想调查定期船内部，\x01",
            "就去找法布利商量吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "他应该在甲板上，\x01",
            "你们可以去看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD")

    label("loc_670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_6ED")

    ChrTalk(    #23
        0xFE,
        (
            "哟，游击士们。\x01",
            "碰到库因特了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "索斯摩夫那家伙\x01",
            "也一定在飞船坪里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "不过我也有一会儿\x01",
            "没见到他了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD")

    label("loc_6ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_74E")

    ChrTalk(    #26
        0xFE,
        (
            "猫的事你们可以去找\x01",
            "操舵手库因特问问。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "他刚出去\x01",
            "吃晚饭了，\x01",
            "应该还在城里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BD")

    label("loc_74E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_75F")
    Call(1, 1)
    Jump("loc_7BD")

    label("loc_75F")


    ChrTalk(    #28
        0xFE,
        (
            "我和大家商量后觉得\x01",
            "至少得重新检查一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "不过，雾这么厉害，\x01",
            "还是准备检查完毕就撤退。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BD")

    TalkEnd(0xA)
    Return()

    # Function_4_542 end

    def Function_5_7C1(): pass

    label("Function_5_7C1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_825")

    ChrTalk(    #30
        0xFE,
        "听说你们找到猫了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "好像还和\x01",
            "小猫在一起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "哎呀～怪不得会\x01",
            "这么热闹。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87B")

    label("loc_825")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_86C")

    ChrTalk(    #33
        0xFE,
        (
            "好了，各位也请\x01",
            "重新振奋精神吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "好了，加油吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_87B")

    label("loc_86C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_87B")
    Call(1, 2)

    label("loc_87B")

    TalkEnd(0xB)
    Return()

    # Function_5_7C1 end

    def Function_6_87F(): pass

    label("Function_6_87F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #35
        (
            "\x07\x05定期船飞船坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往柏斯市\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #36
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　『利贝尔飞船公社』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_87F end

    def Function_7_91B(): pass

    label("Function_7_91B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #37
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "  『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_91B end

    def Function_8_996(): pass

    label("Function_8_996")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        (
            "\x07\x05　※无关人员禁止入内　　\x01",
            "  『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_996 end

    SaveToFile()

Try(main)
