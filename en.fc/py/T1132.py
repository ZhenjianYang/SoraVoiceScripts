from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1132   ._SN',
        MapName             = 'Bose',
        Location            = 'T1132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T1132   ._SN',
            'ED6_DT01/T1132_1 ._SN',
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
        'Barlowe',                              # 9
        'Dina',                                 # 10
        'Hardt',                                # 11
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01120 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190600,
        Direction           = 90,
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
        X                   = -130180,
        Z                   = 0,
        Y                   = 130460,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -86950,
        Z                   = 0,
        Y                   = 119700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 700,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_20A",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_221",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_3AA",          # 05, 5
        "Function_6_B68",          # 06, 6
        "Function_7_1233",         # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_185")
    SetChrPos(0x9, -49700, 0, 119900, 0)
    Jump("loc_209")

    label("loc_185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1A0")
    SetChrPos(0x9, -128400, 0, 139800, 0)
    Jump("loc_209")

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1CC")
    SetChrPos(0x9, -84700, 0, 152800, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9")
    ClearChrFlags(0xA, 0x80)

    label("loc_1C9")

    Jump("loc_209")

    label("loc_1CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1E7")
    SetChrPos(0x9, -84300, 0, 119900, 0)
    Jump("loc_209")

    label("loc_1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_202")
    SetChrPos(0x9, -124300, 0, 179000, 0)
    Jump("loc_209")

    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_209")

    label("loc_209")

    Return()

    # Function_0_16A end

    def Function_1_20A(): pass

    label("Function_1_20A")

    Return()

    # Function_1_20A end

    def Function_2_20B(): pass

    label("Function_2_20B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_220")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_20B")

    label("loc_220")

    Return()

    # Function_2_20B end

    def Function_3_221(): pass

    label("Function_3_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_24E")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_8D(0xFE, -51500, 121100, -47400, 118400, 2000)
    Jump("loc_228")

    label("loc_24B")

    Jump("loc_32C")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_27B")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278")
    OP_8D(0xFE, -130100, 142200, -127100, 126500, 2000)
    Jump("loc_255")

    label("loc_278")

    Jump("loc_32C")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2A8")

    label("loc_282")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A5")
    OP_8D(0xFE, -86300, 154100, -82400, 151500, 2000)
    Jump("loc_282")

    label("loc_2A5")

    Jump("loc_32C")

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2D5")

    label("loc_2AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D2")
    OP_8D(0xFE, -86000, 121200, -81700, 118700, 2000)
    Jump("loc_2AF")

    label("loc_2D2")

    Jump("loc_32C")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_302")

    label("loc_2DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FF")
    OP_8D(0xFE, -126000, 180700, -122800, 177900, 2000)
    Jump("loc_2DC")

    label("loc_2FF")

    Jump("loc_32C")

    label("loc_302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_32C")

    label("loc_309")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C")
    OP_8D(0xFE, -130120, 126680, -127550, 142940, 2000)
    Jump("loc_309")

    label("loc_32C")

    Return()

    # Function_3_221 end

    def Function_4_32D(): pass

    label("Function_4_32D")

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
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D")
    OP_0D()
    OP_A9(0xD)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_38D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E")
    TalkEnd(0x8)
    Return()

    label("loc_39E")

    Call(0, 5)
    OP_8C(0x8, 90, 0)
    Return()

    # Function_4_32D end

    def Function_5_3AA(): pass

    label("Function_5_3AA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    OP_A2(0x0)

    ChrTalk(    #0
        0x8,
        (
            "Placing importance on tradition\x01",
            "as the years go on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "It's a very difficult task...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Or should I work to improve service which\x01",
            "conforms to the needs of the customers,\x01",
            "instead of being bound by old traditions?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_502")

    label("loc_4A1")


    ChrTalk(    #3
        0x8,
        (
            "Placing importance on tradition\x01",
            "as the years go on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "This is a very difficult task...\x02",
    )

    CloseMessageWindow()

    label("loc_502")

    Jump("loc_B64")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(    #5
        0x8,
        (
            "I understand what my young employees\x01",
            "are trying to say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "But it appears that I'm old and\x01",
            "stuck in my ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Ha ha...\x01",
            "Times have sure changed...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B64")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AB")
    OP_A2(0x0)

    ChrTalk(    #8
        0x8,
        "Whew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "In the past, employees worked together\x01",
            "in an effort to gain customer satisfaction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "But the way young kids think these\x01",
            "days sure has changed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "In one way or another things often\x01",
            "don't go as expected...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_6AB")


    ChrTalk(    #12
        0x8,
        (
            "In the past, employees worked together\x01",
            "in an effort to gain customer satisfaction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "But the way young kids think these\x01",
            "days sure has changed...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_746")

    Jump("loc_B64")

    label("loc_749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_8F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_858")
    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "This hotel has maintained a high\x01",
            "level of popularity ever since it\x01",
            "was established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "It may be busy around here,\x01",
            "but this hotel is my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "It is my role as the current manager to\x01",
            "find a future manager who can sustain\x01",
            "these traditions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ED")

    label("loc_858")


    ChrTalk(    #17
        0x8,
        (
            "This hotel has maintained a high\x01",
            "level of popularity ever since it\x01",
            "was established.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "It may be busy around here,\x01",
            "but this hotel is my life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    Jump("loc_B64")

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BC")
    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "Whenever we greet guests,\x01",
            "we do so with utmost sincerity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "And our motto is: Service always\x01",
            "comes with a smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "Furthermore, we should always\x01",
            "work to improve service.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A37")

    label("loc_9BC")


    ChrTalk(    #22
        0x8,
        (
            "Whenever we greet guests,\x01",
            "we do so with utmost sincerity...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "And our motto is: Service always\x01",
            "comes with a smile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A37")

    Jump("loc_B64")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_B08")

    ChrTalk(    #24
        0x8,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "The Frieden Hotel began its business\x01",
            "120 years ago and has a long and\x01",
            "distinguished history here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "Please enjoy our hotel's atmosphere\x01",
            "which is rich with tradition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B64")

    label("loc_B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_B64")

    ChrTalk(    #27
        0x8,
        "Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Please enjoy our hotel's atmosphere\x01",
            "which is rich with tradition.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B64")

    TalkEnd(0x8)
    Return()

    # Function_5_3AA end

    def Function_6_B68(): pass

    label("Function_6_B68")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BA5")

    ChrTalk(    #29
        0xFE,
        (
            "I can't believe how busy things\x01",
            "are today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D14")
    OP_A2(0x1)

    ChrTalk(    #30
        0xFE,
        (
            "I am here to work for myself\x01",
            "and not for the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "The manager says we should act only after\x01",
            "considering the effects of our actions\x01",
            "on the hotel as a whole...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "But worrying about the entire hotel is\x01",
            "supposed to be the manager's job,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "And besides, I'm not here to be\x01",
            "an apprentice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Am I wrong for thinking this way?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DDA")

    label("loc_D14")


    ChrTalk(    #35
        0xFE,
        (
            "The manager says we should act only after\x01",
            "considering the effects of our actions\x01",
            "on the hotel as a whole...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "But worrying about the entire hotel is\x01",
            "supposed to be the manager's job,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDA")

    Jump("loc_122F")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(    #37
        0xFE,
        (
            "I don't care what the manager says,\x01",
            "today I'm leaving on time and\x01",
            "going shopping!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I need to blow off some steam from\x01",
            "the last time he made me work\x01",
            "overtime!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_F7B")

    ChrTalk(    #39
        0xFE,
        "Can you believe this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "The manager made me work when it\x01",
            "was supposed to be my break time!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0xFE,
        (
            "Not to mention, I had a table reserved\x01",
            "at the Anterose restaurant and it was\x01",
            "all for nothing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1066")

    ChrTalk(    #42
        0xFE,
        (
            "I've got a table reserved at the\x01",
            "Anterose restaurant today!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I've been saving up for this day\x01",
            "for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I'm so excited I can hardly breathe.\x01",
            "I've got to hurry up and take care\x01",
            "of my work around here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_11B9")

    ChrTalk(    #45
        0xFE,
        (
            "After I finish work today, I'm going to first\x01",
            "have a meal out on the town and then have\x01",
            "a look at some clothes at the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "A certain clothing store in the market\x01",
            "has been pretty popular recently and\x01",
            "the designs are cute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I've got to check and see if there are any\x01",
            "new fashions out that I don't know about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_122F")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_122F")

    ChrTalk(    #48
        0xFE,
        "I'm so busy today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I want to hurry and finish all these\x01",
            "terrible jobs and then head out on\x01",
            "the town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122F")

    TalkEnd(0x9)
    Return()

    # Function_6_B68 end

    def Function_7_1233(): pass

    label("Function_7_1233")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #50
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1233 end

    SaveToFile()

Try(main)
