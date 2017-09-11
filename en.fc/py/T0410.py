from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0410   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0410.x',
        MapIndex            = 13,
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
        'Franz',                                # 9
        'Hannah',                               # 10
        'Chere',                                # 11
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01030 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01030P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
    )

    DeclNpc(
        X                   = 550,
        Z                   = 0,
        Y                   = 34500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = 36100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = 720,
        TriggerZ            = 0,
        TriggerY            = 33340,
        TriggerRange        = 800,
        ActorX              = 550,
        ActorZ              = 1500,
        ActorY              = 34500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_306",          # 03, 3
        "Function_4_32A",          # 04, 4
        "Function_5_32F",          # 05, 5
        "Function_6_4BE",          # 06, 6
        "Function_7_6E6",          # 07, 7
        "Function_8_7B5",          # 08, 8
        "Function_9_11AD",         # 09, 9
        "Function_10_11C9",        # 0A, 10
        "Function_11_11DB",        # 0B, 11
        "Function_12_14D0",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_64(0x0, 0x1)

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_64(0x0, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    Jump("loc_208")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F4")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    OP_64(0x0, 0x1)
    Jump("loc_208")

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_208")

    label("loc_1FE")

    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)

    label("loc_208")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_21C"),
        (100, "loc_2AF"),
        (102, "loc_2AF"),
        (SWITCH_DEFAULT, "loc_2EE"),
    )


    label("loc_21C")

    SetChrPos(0x101, 400, 0, 22000, 0)
    SetChrPos(0x102, 1600, 0, 22000, 0)
    SetChrPos(0x8, 300, 0, 24400, 180)
    SetChrPos(0x9, 1400, 0, 24900, 180)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearMapFlags(0x1)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_2EE")

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EB")
    SetChrPos(0x8, 450, 0, 32400, 0)
    SetChrPos(0x9, 480, 0, 34510, 180)
    Event(0, 8)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)

    label("loc_2EB")

    Jump("loc_2EE")

    label("loc_2EE")

    Return()

    # Function_0_19A end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    Return()

    # Function_1_2EF end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F0")

    label("loc_305")

    Return()

    # Function_2_2F0 end

    def Function_3_306(): pass

    label("Function_3_306")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_329")
    OP_8D(0xFE, 560, 22800, 2860, 25700, 3000)
    Jump("Function_3_306")

    label("loc_329")

    Return()

    # Function_3_306 end

    def Function_4_32A(): pass

    label("Function_4_32A")

    Call(0, 5)
    Return()

    # Function_4_32A end

    def Function_5_32F(): pass

    label("Function_5_32F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436")
    OP_A2(0x2)

    ChrTalk(    #0
        0x8,
        (
            "You really helped us out this time.\x01",
            "Now we'll be able to get back to\x01",
            "shipping out vegetables like before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "The good news is, there are a lot of\x01",
            "people waiting for our produce.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "We'd better get to work so\x01",
            "they can get what they need!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA")

    label("loc_436")


    ChrTalk(    #3
        0x8,
        (
            "You really helped us out this time.\x01",
            "Now we'll be able to get back to\x01",
            "shipping out vegetables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "We sincerely appreciate it.\x02",
    )

    CloseMessageWindow()

    label("loc_4BA")

    TalkEnd(0x8)
    Return()

    # Function_5_32F end

    def Function_6_4BE(): pass

    label("Function_6_4BE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_588")
    OP_A2(0x3)

    ChrTalk(    #5
        0xFE,
        "Well, if it isn't Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Thanks to you two, the children\x01",
            "have been able to sleep soundly\x01",
            "in their beds again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "People most assuredly need\x01",
            "their sleep.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60F")

    label("loc_588")


    ChrTalk(    #8
        0xFE,
        (
            "Thanks to you two, the children\x01",
            "have been able to sleep soundly\x01",
            "in their beds again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "People most assuredly need\x01",
            "their sleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F")

    Jump("loc_6E2")

    label("loc_612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694")
    OP_A2(0x3)

    ChrTalk(    #10
        0xFE,
        (
            "Estelle and Joshua. The two of\x01",
            "you are now wonderful bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "But, try not to overwork yourselves.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E2")

    label("loc_694")


    ChrTalk(    #12
        0xFE,
        (
            "Come and visit if you have any\x01",
            "free time. We'd be delighted to\x01",
            "have you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2")

    TalkEnd(0x9)
    Return()

    # Function_6_4BE end

    def Function_7_6E6(): pass

    label("Function_7_6E6")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_72F")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #13
        0xFE,
        "Ah, Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "D-Did you come to see me...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7B1")

    label("loc_72F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_7B1")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #15
        0xFE,
        (
            "U-Umm, Joshua. I-I'd like you to\x01",
            "come and play with me again\x01",
            "sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "I'll be waiting for you with Will.\x02",
    )

    CloseMessageWindow()

    label("loc_7B1")

    TalkEnd(0xA)
    Return()

    # Function_7_6E6 end

    def Function_8_7B5(): pass

    label("Function_8_7B5")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_43(0x1, 0x1, 0x0, 0x9)
    OP_43(0x0, 0x1, 0x0, 0xA)
    OP_8E(0x101, 0x12C, 0x0, 0x5F50, 0xBB8, 0x0)
    TurnDirection(0x101, 0x9, 0)
    Sleep(1000)

    ChrTalk(    #17
        0x101,
        "#001FGood afternoon, Mr. and Mrs. Perzel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FHow is everyone getting on\x01",
            "these days?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x9,
        "Well, if it isn't Estelle and Joshua.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #20
        0x8,
        (
            "What brings you to our neck of the\x01",
            "woods? Did you come to see Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#501FWe were actually just chatting\x01",
            "with her outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#010FTo tell you the truth, we're here\x01",
            "on an errand today from the Bracer\x01",
            "Guild.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_6D(-560, 200, 28600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -800, 200, 29120, 180)
    SetChrPos(0x9, 1150, 200, 29120, 180)
    SetChrPos(0x101, -800, 250, 26900, 0)
    SetChrPos(0x102, 1150, 250, 26800, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    OP_22(0x11, 0x0, 0x64)
    OP_3F(0x320, 1)

    AnonymousTalk(    #23
        (
            "\x07\x05Estelle hands Mr. Perzel the guild Referral, and Joshua explains that they are\x01",
            "taking over for their father while he is away.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #24
        0x9,
        "#4PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#4PBut don't you think this job is\x01",
            "a little dangerous for just the\x01",
            "two of you to handle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#4PI agree. I'd feel terrible if one\x01",
            "of you were to get hurt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#006FDon't sweat it.\x01",
            "We're bracers, after all.\x02\x03",

            "#006FAnd taking care of monsters\x01",
            "is right up our alley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#010FThe guild has even authorized us to carry\x01",
            "out this task. If you wouldn't mind leaving\x01",
            "it to us, we'd be more than grateful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "#4PHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#4PWell, all right, then.\x01",
            "Go ahead and have at it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#501FThank you very much, Mr. Perzel!\x02\x03",

            "Then could you tell us a little\x01",
            "more about the monsters that\x01",
            "have been wrecking your fields?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#4PI haven't been able to get a clear look\x01",
            "at one yet...but, they seem to resemble\x01",
            "something like a chubby cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#4PAs far as I can tell, three or four appear at\x01",
            "night and raid our fields, gnawing on anything\x01",
            "they can get their grubby little paws on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#4PThey don't seem threatening exactly,\x01",
            "but they're extremely nimble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "#4PWe've tried many times to capture\x01",
            "them over the course of the last\x01",
            "several nights but to no avail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#002FSounds like a pretty strange bunch\x01",
            "of creatures if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#012FSince they only appear under the\x01",
            "cover of night, we'll have to wait\x01",
            "for it to get dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#4PThen how about taking a load\x01",
            "off until then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#4PI assume you'll also be joining\x01",
            "us for dinner, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#001FYou said the magic word!♪\x01",
            "You bet I will!\x02\x03",

            "#001FI'm a huge fan of your cooking,\x01",
            "Mrs. Perzel. I can't wait!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#4PYou sure know how to please a\x01",
            "woman who spends a lot of time\x01",
            "toiling in the kitchen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#4PAnd for that, I'll whip you up\x01",
            "something special that'll live\x01",
            "up to your expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0401   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_8_7B5 end

    def Function_9_11AD(): pass

    label("Function_9_11AD")

    OP_8E(0x102, 0x578, 0x0, 0x6144, 0xBB8, 0x0)
    TurnDirection(0x102, 0x9, 0)
    Return()

    # Function_9_11AD end

    def Function_10_11C9(): pass

    label("Function_10_11C9")

    OP_6D(0, 0, 28000, 2000)
    Return()

    # Function_10_11C9 end

    def Function_11_11DB(): pass

    label("Function_11_11DB")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)

    ChrTalk(    #43
        0x8,
        (
            "Thank you both.\x01",
            "You did us all a great service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Once again, I apologize for things\x01",
            "not turning out the way they should\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#010FPlease don't worry about it anymore.\x01",
            "We were able to learn a lot from this\x01",
            "experience ourselves.\x02\x03",

            "#010FIf there's anything else we can\x01",
            "help you with in the future,\x01",
            "please let the Bracer Guild know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "That'll definitely be the first place\x01",
            "we contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "We'd love to have you over for the night again\x01",
            "when things are convenient for you. I'll treat you\x01",
            "to some of my best cooking next time you come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#000FThanks for the invitation,\x01",
            "Tio and Mrs. Perzel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#010FWe'll definitely be back to take\x01",
            "you up on that when our work\x01",
            "load settles down.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x0, 0x1, 0x0, 0xC)
    Sleep(800)
    OP_43(0x1, 0x1, 0x0, 0xC)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0400   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_11_11DB end

    def Function_12_14D0(): pass

    label("Function_12_14D0")

    OP_8E(0xFE, 0x3E8, 0x0, 0x5334, 0x5DC, 0x0)
    OP_8E(0xFE, 0x3E8, 0x0, 0x4CF4, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x8)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_14D0 end

    SaveToFile()

Try(main)
