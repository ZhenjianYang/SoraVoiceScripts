from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Emile',                                # 9
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
        "Function_2_F8",           # 02, 2
        "Function_3_10E",          # 03, 3
        "Function_4_18B",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Return()

    # Function_1_F7 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_F8")

    label("loc_10D")

    Return()

    # Function_2_F8 end

    def Function_3_10E(): pass

    label("Function_3_10E")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E")
    OP_0D()
    OP_A9(0xE)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_16E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F")
    TalkEnd(0x8)
    Return()

    label("loc_17F")

    Call(0, 4)
    OP_8C(0x8, 135, 0)
    Return()

    # Function_3_10E end

    def Function_4_18B(): pass

    label("Function_4_18B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1FC")

    ChrTalk(    #0
        0x8,
        (
            "Right now it looks like the orchard\x01",
            "farmers are gathered at the village\x01",
            "elder's house to talk.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    OP_A2(0x0)

    ChrTalk(    #1
        0x8,
        (
            "This village is pretty peaceful except\x01",
            "for the occasional argument between\x01",
            "Gray and Pesca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "It's the same as it was right up\x01",
            "until the Imperial Army invaded\x01",
            "this place 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "This is why we can't help but think\x01",
            "that maybe some day our peace\x01",
            "will be shattered again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6")

    label("loc_330")


    ChrTalk(    #4
        0x8,
        (
            "This village was peaceful right\x01",
            "up until the Imperial Army\x01",
            "invaded 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "This is why we can't help but\x01",
            "think that maybe some day our\x01",
            "peace will be shattered again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6")

    Jump("loc_815")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_492")
    OP_A2(0x0)

    ChrTalk(    #6
        0x8,
        (
            "Some members of the Royal\x01",
            "Army showed up. I wonder\x01",
            "what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I heard that they didn't find anything\x01",
            "in their last investigation...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_501")

    label("loc_492")


    ChrTalk(    #8
        0x8,
        (
            "Whenever we see anybody dressed\x01",
            "in military uniform coming in and out\x01",
            "of this place we get a bit nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501")

    Jump("loc_815")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_64F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F0")
    OP_A2(0x0)

    ChrTalk(    #9
        0x8,
        (
            "I had my own store in the\x01",
            "Bose Market at one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "However, I feel more comfortable\x01",
            "in my hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Unfortunately, this place is out\x01",
            "of the way, and sometimes it's\x01",
            "difficult to get products in stock.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64C")

    label("loc_5F0")


    ChrTalk(    #12
        0x8,
        (
            "I have fond memories of the times\x01",
            "I had in the Bose Market, and I\x01",
            "learned a lot there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C")

    Jump("loc_815")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(    #13
        0x8,
        (
            "Even young children were victims\x01",
            "of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "It still pains me today when\x01",
            "I think about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #15
        0x8,
        (
            "This village is close to the border\x01",
            "and was one of the first places\x01",
            "to be occupied during the war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "There were so many victims back then,\x01",
            "and the deep wounds in peoples' hearts\x01",
            "still have yet to heal over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_7AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_815")

    ChrTalk(    #17
        0x8,
        (
            "Hi there. I don't think I've seen\x01",
            "you around here before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "Welcome to Ravennue Village!\x02",
    )

    CloseMessageWindow()

    label("loc_815")

    OP_56(0x0)
    TalkEnd(0x8)
    Sleep(300)
    Return()

    # Function_4_18B end

    SaveToFile()

Try(main)
