from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1410   ._SN',
        MapName             = 'Bose',
        Location            = 'C1410.x',
        MapIndex            = 62,
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
        'Whemler',                              # 9
        'Lyndon',                               # 10
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
        'ED6_DT07/CH01680 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = 33900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 3410,
        Z                   = 0,
        Y                   = 36700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 4500,
        TriggerZ            = 0,
        TriggerY            = 39460,
        TriggerRange        = 1500,
        ActorX              = 5070,
        ActorZ              = 500,
        ActorY              = 39610,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_146",          # 01, 1
        "Function_2_147",          # 02, 2
        "Function_3_15D",          # 03, 3
        "Function_4_1119",         # 04, 4
        "Function_5_15A5",         # 05, 5
        "Function_6_2E02",         # 06, 6
        "Function_7_2E8B",         # 07, 7
        "Function_8_2F2D",         # 08, 8
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_134")
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x8, 0, 0)
    Jump("loc_145")

    label("loc_134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_145")
    SetChrFlags(0x8, 0x80)

    label("loc_145")

    Return()

    # Function_0_11E end

    def Function_1_146(): pass

    label("Function_1_146")

    Return()

    # Function_1_146 end

    def Function_2_147(): pass

    label("Function_2_147")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_147")

    label("loc_15C")

    Return()

    # Function_2_147 end

    def Function_3_15D(): pass

    label("Function_3_15D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_25B")
    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "I can't help but think there's got to be some kind\x01",
            "of connection between these strange events and\x01",
            "the whole dragon problem from a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Like something's lurking in the shadows, biding\x01",
            "its time until its ready to strike...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1118")

    label("loc_25B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312")

    ChrTalk(    #2
        0xFE,
        "Ah, it's you guys. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I've actually got some company\x01",
            "for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "He says he's a 'dragon researcher,'\x01",
            "here to investigate the ancient dragon's\x01",
            "nest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3AE")

    label("loc_312")


    ChrTalk(    #5
        0xFE,
        (
            "I've actually got some company\x01",
            "for once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "By Aidios'... Out and about at a\x01",
            "time like this. Always curious about\x01",
            "everything little thing, that guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE")

    TalkEnd(0xFE)
    Jump("loc_1118")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_C77")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 1)), scpexpr(EXPR_END)), "loc_538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0")

    ChrTalk(    #7
        0xFE,
        (
            "Sounds like you kids managed to\x01",
            "calm the ancient dragon down without\x01",
            "any problems cropping up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Thanks for that, by the way. Living next\x01",
            "to a raging, flying legend wasn't exactly\x01",
            "something I was looking forward to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_535")

    label("loc_4B0")


    ChrTalk(    #9
        0xFE,
        (
            "Keep an eye on your friends\x01",
            "if you serve that stew, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "It's got some bite to it. Some\x01",
            "folks don't take to it very well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_535")

    Jump("loc_C71")

    label("loc_538")


    ChrTalk(    #11
        0xFE,
        "Ah, it's you guys. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Sounds like you kids managed to\x01",
            "calm the ancient dragon down without\x01",
            "any problems cropping up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Thanks for that, by the way. Living next\x01",
            "to a raging, flying legend wasn't exactly\x01",
            "something I was looking forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006FWe really couldn't have\x01",
            "done it without your help,\x01",
            "Mr. Whemler.\x02\x03",

            "Seriously, we owe you one!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F4")

    ChrTalk(    #15
        0x106,
        (
            "#051FI'll say. We're the ones who\x01",
            "should be thanking you, old-\x01",
            "timer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_6F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_733")

    ChrTalk(    #16
        0x103,
        (
            "#020FYes, thank you for helping us,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_733")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_770")

    ChrTalk(    #17
        0x108,
        "#070FYeah, thanks a lot for your help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_770")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D1")

    ChrTalk(    #18
        0x104,
        (
            "#031FHeh! Indeed.\x02\x03",

            "Allow me to express my most\x01",
            "heartfelt thanks, my good man.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #19
        0xFE,
        (
            "You came all the way out here\x01",
            "just to say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Hmph. Well, don't you have all\x01",
            "the free time in the world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1016FThat's, um, not really the reason we're...\x01",
            "(Though I guess it IS kinda true...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Well, either way, I'm grateful.\x01",
            "If you ever need to take a load\x01",
            "off, you're always welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Also, if you're hungry, feel free\x01",
            "to help yourself to some of the\x01",
            "stew in that pot over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1004FOh! You don't mind if we have\x01",
            "a bite to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Least I can do. Eating that takes\x01",
            "a fair bit of courage, mind you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Still, figure bracers like you\x01",
            "would work up an appetite with\x01",
            "all them scuffles you get into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Anything's worth trying once,\x01",
            "right? Go on, have some.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #28
        "\x06Ate #2CDark Stew (unfortunately)#0C. \x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF3")
    OP_31(0x0, 0x2, 0x1)
    OP_31(0x0, 0x5, 0x0)

    label("loc_AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B06")
    OP_31(0x1, 0x5, 0xC8)

    label("loc_B06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B19")
    OP_31(0x2, 0x5, 0xC8)

    label("loc_B19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2C")
    OP_31(0x3, 0x5, 0xC8)

    label("loc_B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3F")
    OP_31(0x4, 0x5, 0xC8)

    label("loc_B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B52")
    OP_31(0x5, 0x5, 0xC8)

    label("loc_B52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B65")
    OP_31(0x6, 0x5, 0xC8)

    label("loc_B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B78")
    OP_31(0x7, 0x5, 0xC8)

    label("loc_B78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8B")
    OP_31(0x8, 0x5, 0xC8)

    label("loc_B8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x8)"), scpexpr(EXPR_END)), "loc_BA5")
    Jump("loc_BCF")

    label("loc_BA5")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x06Learned #2CDark Stew#0C recipe. \x02",
    )

    CloseMessageWindow()

    label("loc_BCF")

    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0xFE,
        (
            "...Huh. You kids...downed that\x01",
            "like it was nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Come by again any time\x01",
            "you like. You'll always be\x01",
            "welcome under this roof!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A51)
    OP_A2(0x0)

    label("loc_C71")

    TalkEnd(0xFE)
    Jump("loc_1118")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_END)), "loc_D40")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CFA")

    ChrTalk(    #32
        0xFE,
        (
            "There's a lot of dangerous\x01",
            "monsters in those caves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Don't overdo it, you hear?\x01",
            "Be careful out there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A")

    label("loc_CFA")


    ChrTalk(    #34
        0xFE,
        "Came back, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Feel free to rest up if\x01",
            "you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    TalkEnd(0xFE)
    Jump("loc_1118")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 5)), scpexpr(EXPR_END)), "loc_D4E")
    Call(0, 5)
    Jump("loc_1118")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_E75")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE9")

    ChrTalk(    #36
        0xFE,
        (
            "I don't know what could bring\x01",
            "you all the way out here, but\x01",
            "welcome, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Feel free to use anything you\x01",
            "need in here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6F")

    label("loc_DE9")


    ChrTalk(    #38
        0xFE,
        (
            "I don't know what could bring\x01",
            "you all the way out here, but\x01",
            "welcome, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Feel free to use anything you\x01",
            "need in here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6F")

    TalkEnd(0xFE)
    Jump("loc_1118")

    label("loc_E75")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        "Well, well! Who're you kids?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1011FPardon us, sir, we're from the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #42
        0xFE,
        "Yes, I can see that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #43
        0xFE,
        (
            "And I also see a certain red-haired\x01",
            "brat who's standing over here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x106,
        (
            "#053FHeh. Who're you still calling a brat,\x01",
            "you old fossil?\x02\x03",

            "#051FThough, really, good to see you,\x01",
            "Whemler.\x02\x03",

            "You holdin' up okay out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Heh heh! I'm doing well enough\x01",
            "to be able to keep up with you\x01",
            "kids, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I don't know what could bring\x01",
            "you all the way out here, but\x01",
            "welcome, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Feel free to use anything you\x01",
            "need in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1018FCool! Thank you, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#051FSorry for the trouble, old-timer.\x01",
            "And thanks.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A80)
    OP_A2(0x0)
    TalkEnd(0xFE)

    label("loc_1118")

    Return()

    # Function_3_15D end

    def Function_4_1119(): pass

    label("Function_4_1119")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_139C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CB")

    ChrTalk(    #50
        0xFE,
        (
            "As one who studies the creatures of\x01",
            "old, I have to admit that I'm tremendously\x01",
            "curious about the ancient dragon's nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Mr. Whemler here stopped me from going\x01",
            "because it's too dangerous, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Apparently, the only ones who've\x01",
            "successfully managed to get past\x01",
            "this point have been bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I'll admit, I don't think I have\x01",
            "bracer levels of tenacity. Can't\x01",
            "imagine I'd fare half as well. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1399")

    label("loc_12CB")


    ChrTalk(    #54
        0xFE,
        (
            "It seems the only ones to have\x01",
            "successfully explored the dragon's\x01",
            "nest so far are bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "And, well, recent events make clear\x01",
            "that they're the only ones who COULD\x01",
            "explore such a dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1399")

    Jump("loc_15A1")

    label("loc_139C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F3")

    ChrTalk(    #56
        0xFE,
        (
            "Hello there! I'm just your\x01",
            "run-of-the-mill archaeobiologist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "A little birdie told me there's a\x01",
            "dragon's nest nearby, and so,\x01",
            "out the door I went!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Unfortunately, it looks to be a rather\x01",
            "dangerous place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "That's why I'm here instead of there.\x01",
            "I'm just, um, biding my time here for\x01",
            "the moment, I suppose. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_15A1")

    label("loc_14F3")


    ChrTalk(    #60
        0xFE,
        (
            "I heard there's a dragon's\x01",
            "nest nearby, so I came to\x01",
            "out here to take a look...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Unfortunately, it looks to\x01",
            "be a rather dangerous place.\x01",
            "I can't bring myself to go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A1")

    TalkEnd(0x9)
    Return()

    # Function_4_1119 end

    def Function_5_15A5(): pass

    label("Function_5_15A5")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BC")
    Call(0, 6)
    Call(0, 8)

    label("loc_15BC")

    Fade(1000)
    OP_6D(3740, 0, 36060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 4260, 0, 35660, 225)
    SetChrPos(0x106, 3350, 0, 36130, 180)
    SetChrPos(0x107, 2660, 0, 36470, 180)
    SetChrPos(0xF9, 3440, 0, 37310, 180)
    OP_4A(0x8, 255)
    OP_0D()
    TurnDirection(0xF9, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Whemler in the previous game\x01",              # 0
            "Set as didn't meet Whemler in the previous game\x01",      # 1
            "No change\x01",                                            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16FF"),
        (1, "loc_1705"),
        (SWITCH_DEFAULT, "loc_170B"),
    )


    label("loc_16FF")

    OP_A2(0x1A80)
    Jump("loc_170B")

    label("loc_1705")

    OP_A3(0x1A80)
    Jump("loc_170B")

    label("loc_170B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 0)), scpexpr(EXPR_END)), "loc_1821")

    ChrTalk(    #62
        0x106,
        "#051FYo, Old-timer!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(700)

    ChrTalk(    #63
        0x8,
        "#4POh... Agate. And the little sprout's group.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1011F#6PHello, Mr. Whemler.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        "#560F#6PUm, sorry to bother you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#4PHmmm. You kids seem like you're filled\x01",
            "with purpose this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#4PWhat's happened? Tell me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A66")

    label("loc_1821")

    OP_8C(0x8, 0, 400)
    Sleep(700)

    ChrTalk(    #68
        0x8,
        "#4PHmm? Who're you sprouts?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        "#560F#6PSorry to bother you, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1011F#6PPardon us, sir, we're from the\x01",
            "Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "#4PYes, I can see that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#4PAnd I suppose I know this red-haired brat\x01",
            "who's standing over here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#053FHeh. Who you still callin' a brat,\x01",
            "you old fossil?\x02\x03",

            "#051FThough, really, good to see you, Whemler.\x02\x03",

            "You holdin' up okay out here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#4PHeheh. I'm doing well enough to be able\x01",
            "to keep up with you kids, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#4PMore importantly, what brings you out here?\x01",
            "Seems like you kids are filled with purpose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A66")


    ChrTalk(    #76
        0x101,
        "#1002F#6PYes, we are, sir. Actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        (
            "\x07\x05Estelle explained about the dragon attacks around the region\x01",
            "and how it disappeared into the northwest part of the\x01",
            "valley.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #78
        0x8,
        "#4POhhhh... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#4PExplains all the noise a little while ago,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#051FHey, Old-timer.\x02\x03",

            "You used to say you've been to\x01",
            "the northwest, right?\x02\x03",

            "If you don't mind, we'd like to\x01",
            "know what route you used.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #81
        0x8,
        "#4PAbsolutely not.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D07")

    label("loc_1CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF0")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1D07")

    label("loc_1CF0")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1D07")

    Sleep(1000)

    ChrTalk(    #82
        0x101,
        "#1004F#6PHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        "#055FThe hell?! Why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "#4P...Let me ask you kids one question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#4POnce you find that dragon,\x01",
            "what're you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1015F#6POh, u-um...\x02\x03",

            "It seems like it's being controlled,\x01",
            "so we don't really want to slay it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x106,
        (
            "#552FBut if it keeps causing trouble even after\x01",
            "we break the Gospel, we'll have to.\x02\x03",

            "Can't let it hurt people no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#4PGoodness...\x01",
            "Children today know nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#4PYou kids are treating that dragon\x01",
            "as if it's just a big monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        "#4PThat's no dumb beast you're hunting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#4PThat is a divine creature older than\x01",
            "the Great Collapse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1015F#6PFrom before the Gr--\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #93
        0x101,
        "#1020F#6P#3SWH-WHAAAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #94
        0x107,
        (
            "#065F#6PYou're saying it's been here for over\x01",
            "twelve hundred years?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x106,
        (
            "#051FHaha. C'mon, Old-timer, be serious.\x02\x03",

            "Sure, it might have a long lifespan, but--\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2162")

    ChrTalk(    #96
        0x103,
        (
            "#025F#6PNo, I actually think Mr. Whemler may be right.\x02\x03",

            "#022FFew countries still have legends of dragons...\x02\x03",

            "But in every one I've encountered,\x01",
            "they're said to be long-lived to the point\x01",
            "of being ageless and immortal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2433")

    label("loc_2162")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_227F")

    ChrTalk(    #97
        0x105,
        (
            "#043F#6PNo. I fear Mr. Whemler may be correct.\x02\x03",

            "There are records of sighting of dragons\x01",
            "that go back as far as nine hundred years,\x01",
            "to Liberl's founding.\x02\x03",

            "Apparently they used to show themselves\x01",
            "more often...and many of the reports are,\x01",
            "um, suspiciously uniform.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2433")

    label("loc_227F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(    #98
        0x104,
        (
            "#035F#6PMr. Whemler speaks the truth, I believe.\x02\x03",

            "#032FAccording to the legends of the Septian\x01",
            "Church, dragons are the divine guardians\x01",
            "of She Who Dwells Above.\x02\x03",

            "I find it unlikely we can apply our\x01",
            "common experience to them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2433")

    label("loc_2376")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2433")

    ChrTalk(    #99
        0x108,
        (
            "#074F#6PMr. Whemler speaks the truth, I think.\x02\x03",

            "#072FIn the East, dragons are worshiped as\x01",
            "heavenly beasts.\x02\x03",

            "We should think of them as being beyond\x01",
            "normal human reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2433")

    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #100
        0x106,
        "#055FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1007F#6PI'm, uh, starting to think we shouldn't have\x01",
            "thought of it like a normal monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#4PTrying to 'slay' that creature would be\x01",
            "nothing but suicide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "#4PSo be good and leave it to the Royal Army.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#4PHonestly, most of the army's got their\x01",
            "heads up their ends, too, but maybe he\x01",
            "could...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#4P...Anyway. I've no desire to send\x01",
            "young people to their graves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        "#4PI'm sorry, but I can't help you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1026F#6PBut...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#053F...\x02\x03",

            "#555FHey, Old-timer.\x02\x03",

            "I appreciate the concern, but you're\x01",
            "a bit off the mark, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        "#4PMm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x106,
        (
            "#050FWe've fought a lot of nasty stuff to\x01",
            "get this far.\x02\x03",

            "Intelligence Division thugs, ancient\x01",
            "orbal machines...\x02\x03",

            "#053FNasty as they were, though, we couldn't just\x01",
            "let 'em go 'cause they were 'too dangerous.'\x02\x03",

            "We put together what we had, every one\x01",
            "of us gave it our all, and we managed to\x01",
            "overcome them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        "#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        (
            "#051FThis dragon's the same.\x02\x03",

            "We ain't just gonna blindly rush in...\x01",
            "but we can't let this go, either.\x02\x03",

            "#053FSo...please.\x02\x03",

            "Lend us a hand. We need you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #114
        0x101,
        "#1025F#4PAgate...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)
    Sleep(300)

    ChrTalk(    #115
        0x107,
        "#560F#6PAgate...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        "#4PHeheh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#4PFinally got a bit of nobility on that ugly mug\x01",
            "of yours, eh? Your sister'd like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#4PWell, after a speech like that,\x01",
            "guess I have no choice but to\x01",
            "help, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        "#052F!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #120
        0x101,
        "#1004F#6PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#067F#6PThank you, Mr. Whemler!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "#4PNah, don't worry about it.\x01",
            "I'm not doing anything that big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        "#4PI'll head out first and get things ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#4PCome find me when you're ready,\x01",
            "I'll be at the deepest point of\x01",
            "the western side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015F#6PCome find you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x106,
        (
            "#555FWait, weren't you going to tell us how\x01",
            "to get to the northwest part of--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#4PIt's going to involve a bit more than\x01",
            "just telling you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "#4PAnyway, come as soon as you can to the\x01",
            "west side by foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        "#4PI'll be waiting.\x02",
    )

    CloseMessageWindow()

    def lambda_2BCA():

        label("loc_2BCA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2BCA")

    QueueWorkItem2(0x101, 1, lambda_2BCA)

    def lambda_2BDB():

        label("loc_2BDB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2BDB")

    QueueWorkItem2(0x106, 1, lambda_2BDB)

    def lambda_2BEC():

        label("loc_2BEC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2BEC")

    QueueWorkItem2(0x107, 1, lambda_2BEC)

    def lambda_2BFD():

        label("loc_2BFD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2BFD")

    QueueWorkItem2(0xF9, 1, lambda_2BFD)

    def lambda_2C0E():
        OP_6D(2020, 0, 36590, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C0E)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xCC6, 0x0, 0x8886, 0xBB8, 0x0)
    OP_8E(0x8, 0x500, 0x0, 0x8DA4, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFFEE26, 0x0, 0x8C50, 0xBB8, 0x0)

    def lambda_2C67():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C67)
    OP_8E(0x8, 0xFFFFEA8E, 0x0, 0x8C0A, 0xBB8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    ChrTalk(    #130
        0x101,
        "#1020F#4PW-Wait!\x02",
    )

    CloseMessageWindow()
    OP_6D(3740, 0, 36060, 1500)

    ChrTalk(    #131
        0x106,
        (
            "#551F#6P...Nothin' for it.\x02\x03",

            "#050FLike the old man said,\x01",
            "we should get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007F#4PRight, right.\x02\x03",

            "#1002FDeepest point of the west side\x01",
            "of the valley, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D7D():
        OP_8C(0x107, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2D7D)

    def lambda_2D8B():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2D8B)
    OP_8C(0x106, 90, 400)
    Sleep(500)

    ChrTalk(    #133
        0x106,
        (
            "#051F#6PYeah.\x02\x03",

            "Need to keep an eye out so that\x01",
            "we don't get lost out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A26)
    OP_28(0x96, 0x1, 0x40)
    OP_28(0x96, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_15A5 end

    def Function_6_2E02(): pass

    label("Function_6_2E02")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E7E"),
        (1, "loc_2E84"),
        (SWITCH_DEFAULT, "loc_2E8A"),
    )


    label("loc_2E7E")

    OP_A2(0x1200)
    Jump("loc_2E8A")

    label("loc_2E84")

    OP_A2(0x1201)
    Jump("loc_2E8A")

    label("loc_2E8A")

    Return()

    # Function_6_2E02 end

    def Function_7_2E8B(): pass

    label("Function_7_2E8B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F11")
    SoundLoad(13)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F2B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F2B")

    Return()

    # Function_7_2E8B end

    def Function_8_2F2D(): pass

    label("Function_8_2F2D")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_8_2F2D end

    SaveToFile()

Try(main)
