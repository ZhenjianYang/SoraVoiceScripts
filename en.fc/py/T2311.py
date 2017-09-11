from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2311   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
        'Boy',                                  # 12
        'Boy',                                  # 13
        'Boy',                                  # 14
        'Boy',                                  # 15
        'Boy',                                  # 16
        'Boy',                                  # 17
        'Steward Gilbert',                      # 18
        'Carna',                                # 19
        'Amelia',                               # 20
        'Zack',                                 # 21
        'Solomon',                              # 22
        'Elder Serge',                          # 23
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
        'ED6_DT07/CH00374 ._CH',             # 00
        'ED6_DT07/CH02420 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH00374P._CP',             # 00
        'ED6_DT07/CH02420P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
    )

    DeclNpc(
        X                   = -31270,
        Z                   = 0,
        Y                   = 42780,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30310,
        Z                   = 0,
        Y                   = 42270,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -28770,
        Z                   = 0,
        Y                   = 42770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -31020,
        Z                   = 0,
        Y                   = 44700,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30070,
        Z                   = 0,
        Y                   = 44130,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -29310,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -31330,
        Z                   = 0,
        Y                   = 43790,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30780,
        Z                   = 0,
        Y                   = 43810,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30050,
        Z                   = 0,
        Y                   = 43240,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -26650,
        Z                   = 0,
        Y                   = 44050,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -30050,
        Z                   = 0,
        Y                   = 39240,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -200,
        Z                   = 0,
        Y                   = 8850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 5500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 0,
        Y                   = 5700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -26100,
        Z                   = 0,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_2C2",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_3F4",          # 02, 2
        "Function_3_40A",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_69C",          # 05, 5
        "Function_6_738",          # 06, 6
        "Function_7_862",          # 07, 7
        "Function_8_8C4",          # 08, 8
    )


    def Function_0_2C2(): pass

    label("Function_0_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2CC")
    Jump("loc_374")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_309")
    SetChrPos(0x14, -26670, 0, 39530, 90)
    SetChrPos(0x16, -30150, 0, 3860, 270)
    SetChrPos(0x15, -29310, 0, 43880, 0)
    Jump("loc_374")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_313")
    Jump("loc_374")

    label("loc_313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_331")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_374")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_34F")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8)
    Jump("loc_374")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_374")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_374")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_36D")
    Jump("loc_374")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8)

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_3F2")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_3F2")

    Return()

    # Function_0_2C2 end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Return()

    # Function_1_3F3 end

    def Function_2_3F4(): pass

    label("Function_2_3F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_409")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F4")

    label("loc_409")

    Return()

    # Function_2_3F4 end

    def Function_3_40A(): pass

    label("Function_3_40A")

    TalkBegin(0x13)

    ChrTalk(    #0
        0xFE,
        (
            "Zack went to the Bracer Guild to tell\x01",
            "them what he knows. Now he's back, and\x01",
            "helping out at the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "He's a good brother. Always\x01",
            "dependable when the chips\x01",
            "are down.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x13)
    Return()

    # Function_3_40A end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "Did you find out the\x01",
            "criminals' identities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "We can't let anyone who would\x01",
            "do something like this get away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "You make sure you catch them and show them\x01",
            "the error of their ways...as politely as\x01",
            "you can with your preferred weapon of choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_698")

    label("loc_5CD")


    ChrTalk(    #5
        0xFE,
        (
            "We can't let anyone who would\x01",
            "do something like this get away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "You make sure you catch them and show them\x01",
            "the error of their ways...as politely as\x01",
            "you can with your preferred weapon of choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698")

    TalkEnd(0x14)
    Return()

    # Function_4_4C0 end

    def Function_5_69C(): pass

    label("Function_5_69C")

    TalkBegin(0x15)

    ChrTalk(    #7
        0xFE,
        (
            "I was thinking, I can at least get\x01",
            "the children something to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Carla asked me to fetch her some\x01",
            "ingredients to make them a hearty\x01",
            "meal.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x15)
    Return()

    # Function_5_69C end

    def Function_6_738(): pass

    label("Function_6_738")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")
    OP_A2(0x3)

    ChrTalk(    #9
        0xFE,
        (
            "We simply cannot allow an\x01",
            "atrocity like this to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "All of the villagers are willing\x01",
            "to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Please, catch whoever did this...\x01",
            "for the children's sakes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85E")

    label("loc_7F4")


    ChrTalk(    #12
        0xFE,
        (
            "We simply cannot allow an\x01",
            "atrocity like this to pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "All of the villagers are willing\x01",
            "to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85E")

    TalkEnd(0x16)
    Return()

    # Function_6_738 end

    def Function_7_862(): pass

    label("Function_7_862")

    TalkBegin(0x12)

    ChrTalk(    #14
        0x12,
        (
            "I'll stand guard over the village.\x02\x03",

            "You should go back to Ruan\x01",
            "and report in to Jean.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_7_862 end

    def Function_8_8C4(): pass

    label("Function_8_8C4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-29840, 0, 41310, 0)
    RemoveParty(0x5, 0xFF)
    SetChrPos(0x101, -29970, 0, 37680, 0)
    SetChrPos(0x102, -30850, 0, 37060, 0)
    SetChrPos(0x105, -29450, 0, 36780, 0)
    OP_8C(0x12, 180, 0)

    ChrTalk(    #15
        0x12,
        (
            "Now then... I'll keep an eye on\x01",
            "things here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "Could you return to Ruan and\x01",
            "report back to Jean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#000FThat's fine with me, but are\x01",
            "you sure you'll be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "C'mon, I just got a whiff of\x01",
            "sleeping powder is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "It's pretty pathetic, though.\x01",
            "I can't believe I let those\x01",
            "idiots get the better of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#010FDon't beat yourself up over it.\x02\x03",

            "You still managed to defeat\x01",
            "four attackers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#040FThe children are safe thanks to\x01",
            "you.\x02\x03",

            "I can't thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "Ha ha... Well, I guess there's\x01",
            "that, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "Still, will Agate be okay, facing\x01",
            "them on his own?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "I know he's tough and all,\x01",
            "but it still worries me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#000FY-Yeah... If they somehow\x01",
            "manage to get the drop on\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#010FFor now, we just have to trust\x01",
            "that he knows what he's doing. \x02\x03",

            "He's been after those guys\x01",
            "for a long time.\x02\x03",

            "He knows how they work, so I think\x01",
            "they'll have a tough time taking\x01",
            "him on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#000FYeah, I guess you're right!\x02\x03",

            "We'll just have to focus on\x01",
            "what WE can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x12,
        (
            "You're right.\x01",
            "You're exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "I'll hang on to the donated money until the\x01",
            "matron wakes up. If those guys want it, they'll\x01",
            "have to pry it from my cold, dead fingers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "You can count on me. I'll be\x01",
            "fine, so you go on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x105,
        "#040FAll right...be careful.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #32
        0x101,
        "#000FLet's go, guys!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_8_8C4 end

    SaveToFile()

Try(main)
