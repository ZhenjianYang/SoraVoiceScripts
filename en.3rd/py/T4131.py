from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4131   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Archbishop Currant',                   # 9
        'Father Reval',                         # 10
        'Sister Noah',                          # 11
        'Cisna',                                # 12
        'May',                                  # 13
        'Nielsen',                              # 14
        'Erika Russell',                        # 15
        'Lt. Colonel Cid',                      # 16
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
        'ED6_DT07/CH01670 ._CH',             # 01
        'ED6_DT07/CH01410 ._CH',             # 02
        'ED6_DT07/CH01033 ._CH',             # 03
        'ED6_DT27/CH03970 ._CH',             # 04
        'ED6_DT27/CH03590 ._CH',             # 05
        'ED6_DT07/CH02490 ._CH',             # 06
        'ED6_DT07/CH01660 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01670P._CP',             # 01
        'ED6_DT07/CH01410P._CP',             # 02
        'ED6_DT07/CH01033P._CP',             # 03
        'ED6_DT27/CH03970P._CP',             # 04
        'ED6_DT27/CH03590P._CP',             # 05
        'ED6_DT07/CH02490P._CP',             # 06
        'ED6_DT07/CH01660P._CP',             # 07
    )

    DeclNpc(
        X                   = -50,
        Z                   = 1000,
        Y                   = 20410,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2870,
        Z                   = 1000,
        Y                   = 18870,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -7950,
        Z                   = 0,
        Y                   = 1210,
        Direction           = 270,
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
        X                   = -3190,
        Z                   = 150,
        Y                   = 10800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5220,
        Z                   = 0,
        Y                   = 3260,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -131950,
        Z                   = 0,
        Y                   = 2700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 200,
        TriggerZ            = 1000,
        TriggerY            = 17890,
        TriggerRange        = 400,
        ActorX              = -50,
        ActorZ              = 2500,
        ActorY              = 20410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74990,
        TriggerZ            = 0,
        TriggerY            = 66030,
        TriggerRange        = 800,
        ActorX              = -74990,
        ActorZ              = 1000,
        ActorY              = 66030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_232",          # 00, 0
        "Function_1_270",          # 01, 1
        "Function_2_27A",          # 02, 2
        "Function_3_27F",          # 03, 3
        "Function_4_52A",          # 04, 4
        "Function_5_6F4",          # 05, 5
        "Function_6_8DA",          # 06, 6
        "Function_7_A40",          # 07, 7
        "Function_8_A96",          # 08, 8
        "Function_9_FAF",          # 09, 9
        "Function_10_FFE",         # 0A, 10
        "Function_11_1857",        # 0B, 11
        "Function_12_188E",        # 0C, 12
    )


    def Function_0_232(): pass

    label("Function_0_232")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_26F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_26F")

    Return()

    # Function_0_232 end

    def Function_1_270(): pass

    label("Function_1_270")

    OP_B1("t4131_n")
    Return()

    # Function_1_270 end

    def Function_2_27A(): pass

    label("Function_2_27A")

    Call(0, 3)
    Return()

    # Function_2_27A end

    def Function_3_27F(): pass

    label("Function_3_27F")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_50B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_363")

    ChrTalk(    #0
        0x10,
        (
            "It may be necessary at times to pluck up the\x01",
            "courage to look back at the path we've tread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "Still, there is nothing to be afraid of in doing so.\x01",
            "Aidios will always show us the way if we look to\x01",
            "Her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_508")

    label("loc_363")


    ChrTalk(    #2
        0x10,
        (
            "At times, all of us lose our way. That in itself\x01",
            "is nothing to be feared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "What is truly terrifying is not noticing that it has\x01",
            "happened, or realizing and willingly turning one's\x01",
            "eyes from that truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "It may be necessary at times to pluck up the\x01",
            "courage to look back at the path we've tread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "Still, there is nothing to be afraid of in doing so.\x01",
            "Aidios will always show us the way if we look to\x01",
            "Her.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_508")

    Jump("loc_526")

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_515")
    Jump("loc_526")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_51F")
    Jump("loc_526")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_526")

    label("loc_526")

    TalkEnd(0x10)
    Return()

    # Function_3_27F end

    def Function_4_52A(): pass

    label("Function_4_52A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_6D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5E9")

    ChrTalk(    #6
        0xFE,
        (
            "It's been five whole years now since the war\x01",
            "came to an end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Oh, Aidios, please grant peace to all those who\x01",
            "lost their lives during that terrible conflict...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D2")

    label("loc_5E9")


    ChrTalk(    #8
        0xFE,
        (
            "Many people came flocking to this cathedral in\x01",
            "search of safety during the Hundred Days War,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "That's no surprise, of course. To the people of\x01",
            "the time, Grancel, protected by the Ahnenburg\x01",
            "Wall, was their final hope.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_6D2")

    Jump("loc_6F0")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_6DF")
    Jump("loc_6F0")

    label("loc_6DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_6E9")
    Jump("loc_6F0")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_6F0")

    label("loc_6F0")

    TalkEnd(0xFE)
    Return()

    # Function_4_52A end

    def Function_5_6F4(): pass

    label("Function_5_6F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7AD")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #10
        0xFE,
        (
            "Ugh... Doing all of this cleaning alone takes\x01",
            "foreeever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "It was so much faster when I had Sister Rosa\x01",
            "to help me. We were always done in a flash...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_7AD")


    ChrTalk(    #12
        0xFE,
        (
            "This cathedral is one of the oldest buildings in\x01",
            "Liberl, incidentally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "It's stood here for hundreds of years, acting as\x01",
            "a guiding light for the people of this nation for\x01",
            "generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "...It's also very large, which makes cleaning it\x01",
            "all a mega pain.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_8B8")

    Jump("loc_8D6")

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8C5")
    Jump("loc_8D6")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8CF")
    Jump("loc_8D6")

    label("loc_8CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8D6")

    label("loc_8D6")

    TalkEnd(0xFE)
    Return()

    # Function_5_6F4 end

    def Function_6_8DA(): pass

    label("Function_6_8DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_94B")

    ChrTalk(    #15
        0xFE,
        "Wh-What?! Is that the time already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I need to get back and help with the cooking!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1E")

    label("loc_94B")


    ChrTalk(    #17
        0xFE,
        (
            "Sisters of the church sure are amazing,\x01",
            "aren't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "They spend their days offering prayers to the\x01",
            "Goddess so that we might be able to live our\x01",
            "lives in peace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "*sigh* What a wonderful job...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_A1E")

    Jump("loc_A3C")

    label("loc_A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A2B")
    Jump("loc_A3C")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A35")
    Jump("loc_A3C")

    label("loc_A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A3C")

    label("loc_A3C")

    TalkEnd(0xFE)
    Return()

    # Function_6_8DA end

    def Function_7_A40(): pass

    label("Function_7_A40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A77")

    ChrTalk(    #20
        0xFE,
        "Oh, Aidios... Please guide us all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A92")

    label("loc_A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A81")
    Jump("loc_A92")

    label("loc_A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A8B")
    Jump("loc_A92")

    label("loc_A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A92")

    label("loc_A92")

    TalkEnd(0xFE)
    Return()

    # Function_7_A40 end

    def Function_8_A96(): pass

    label("Function_8_A96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EB, 1)), scpexpr(EXPR_END)), "loc_C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B19")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #21
        0xFE,
        "So this is Grancel Cathedral...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "It has a truly solemn air to it that even I can\x01",
            "sense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_B19")


    ChrTalk(    #23
        0xFE,
        (
            "I'm due to meet someone here. I'm just waiting\x01",
            "for them to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I'm planning on doing some research on Liberl\x01",
            "while I'm here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "After all, this is the nation now known for\x01",
            "repelling the mighty Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'm eager to see if I can find exactly where\x01",
            "that strength came from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Haha. This should prove to be some very \x01",
            "interesting research!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_C93")

    Jump("loc_F8D")

    label("loc_C96")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #28
        0xFE,
        "Oh? Who might the two of you be?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)
    Sleep(300)

    ChrTalk(    #29
        0xFE,
        (
            "The sound of your footsteps is unfamiliar to me...\x01",
            "I presume this must be the first time we've met?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#1643FY-Yes. It certainly is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x151,
        (
            "#1653FUmm...\x02\x03",

            "#1650FAm I correct in assuming that you must be\x01",
            "visually impaired, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Yes, I am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "If you'll forgive me for saying so, you're a rather\x01",
            "unusual pair, aren't you? One of you is a bracer,\x01",
            "I believe?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0xFE,
        (
            "Haha. There's no need to be so surprised. The air\x01",
            "you have about you reminds me of other bracers\x01",
            "I know, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "I may have lost my vision, but that has allowed me\x01",
            "to see things in a way I couldn't before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        "#1643FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x151,
        "#1650FThat's incredible...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F59)

    label("loc_F8D")

    Jump("loc_FAB")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_F9A")
    Jump("loc_FAB")

    label("loc_F9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_FA4")
    Jump("loc_FAB")

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_FAB")

    label("loc_FAB")

    TalkEnd(0xFE)
    Return()

    # Function_8_A96 end

    def Function_9_FAF(): pass

    label("Function_9_FAF")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_9_FAF end

    def Function_10_FFE(): pass

    label("Function_10_FFE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 850, 0, 14500, 180)
    OP_4A(0x10, 255)
    SetChrPos(0x10, -360, 0, 14000, 180)
    SetChrFlags(0x109, 0x80)
    SetChrPos(0x109, 840, -250, -3240, 0)
    SetChrPos(0x17, -610, -250, -3250, 0)
    OP_6D(-600, 0, 280, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(295, 0)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0xB)
    OP_43(0x17, 0x0, 0x0, 0xC)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(300)

    NpcTalk(    #39
        0x10,
        "Old Man's Voice",
        "#3PAh, there you are.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_111B():
        OP_6D(-730, 0, 14290, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_111B)

    def lambda_1133():
        OP_67(0, 4300, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1133)

    def lambda_114B():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_114B)

    def lambda_115B():
        OP_6E(290, 4000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_115B)
    Sleep(300)

    def lambda_1170():
        OP_8E(0xFE, 0x2DA, 0x0, 0x2E18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1170)
    Sleep(300)

    def lambda_1190():
        OP_8E(0xFE, 0xFFFFFED4, 0x0, 0x2BC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1190)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x17, 0x0)

    ChrTalk(    #40
        0x109,
        (
            "#1060F#6PIt's good to see you again, Archbishop. \x01",
            "You look very well.\x02\x03",

            "#1064FHuh? And you must be...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1224():
        OP_6D(-730, 0, 13900, 800)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1224)
    OP_8E(0x16, 0x28A, 0x0, 0x34BC, 0x5DC, 0x0)
    WaitChrThread(0x16, 0x1)
    Sleep(300)

    NpcTalk(    #41
        0x16,
        "Woman in White",
        (
            "#1450F#2PHmm... I wasn't expecting you to be quite\x01",
            "THIS young.\x02\x03",

            "How old are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1064F#6PDwuh?\x02\x03",

            "Tw-Twenty two, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x16,
        "Woman in White",
        (
            "#1457F#2PThat's a lot younger than I expected.\x02\x03",

            "#1452FAre the Gralsritter really so short-staffed that\x01",
            "they're handing out their most important posts\x01",
            "to kids?\x02\x03",

            "You can't blame me for assuming the Fifth\x01",
            "Dominion would look like more of a veteran,\x01",
            "can you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x109,
        "#1063F#6P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x16,
        "Woman in White",
        (
            "#1458F#2PHeh. Your surprise is written all over your face.\x02\x03",

            "#1456FSomeone in your position should have a much\x01",
            "better poker face than that. Maybe you need to\x01",
            "redo your training from scratch?\x02\x03",

            "Or are you just acting, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        "#1063F#6PHow do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "#703F#6P*sigh* Professor Russell, please...\x02\x03",

            "#701FHe isn't here for you to try and pick a fight with\x01",
            "him. Please try and be a little less deliberately\x01",
            "provocative. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        "#1064F#6PWha...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x16,
        "Woman in White",
        "#1832F#2P#3SHell. No.#2S\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #50
        0x16,
        "Woman in White",
        (
            "#1457F#2PHe's here to steal the thing we went through\x01",
            "so much effort to bring up, and you want me\x01",
            "to play nice?\x02\x03",

            "#1459FAnd kindly don't call me THAT ever again.\x02\x03",

            "I don't want to be addressed in the same way\x01",
            "as that old coot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        "#701F#6P...Of course, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1064F#6PW-Wait. Russell?\x02\x03",

            "Then are you...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #53
        0x16,
        "Woman in White",
        "#1458F#2PHeh. I suppose I should introduce myself.\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #54
        0x16,
        "Erika Russell",
        (
            "#1456F#2PI'm Erika Russell.\x02\x03",

            "I'm sure it's not a name you're going to be\x01",
            "forgetting any time soon.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_10_FFE end

    def Function_11_1857(): pass

    label("Function_11_1857")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_186D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186D)
    OP_8E(0xFE, 0x32A, 0x0, 0xFFFFFAA6, 0x7D0, 0x0)
    Return()

    # Function_11_1857 end

    def Function_12_188E(): pass

    label("Function_12_188E")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_18A9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18A9)
    OP_8E(0xFE, 0xFFFFFDD0, 0x0, 0xFFFFF86C, 0x7D0, 0x0)
    Return()

    # Function_12_188E end

    SaveToFile()

Try(main)
