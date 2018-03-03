from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5408   ._SN',
        MapName             = 'Other',
        Location            = 'C5408.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'Dragion',                              # 9
        'Dragion',                              # 10
        'Loewe',                                # 11
        'Bleublanc',                            # 12
        'Luciola',                              # 13
        'Walter',                               # 14
        'Target Camera',                        # 15
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20243 ._CH',             # 00
        'ED6_DT07/CH02040 ._CH',             # 01
        'ED6_DT27/CH03530 ._CH',             # 02
        'ED6_DT27/CH03520 ._CH',             # 03
        'ED6_DT26/CH20280 ._CH',             # 04
        'ED6_DT26/CH20762 ._CH',             # 05
        'ED6_DT26/CH20761 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT26/CH20243P._CP',             # 00
        'ED6_DT07/CH02040P._CP',             # 01
        'ED6_DT27/CH03530P._CP',             # 02
        'ED6_DT27/CH03520P._CP',             # 03
        'ED6_DT26/CH20280P._CP',             # 04
        'ED6_DT26/CH20762P._CP',             # 05
        'ED6_DT26/CH20761P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0xC5,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1F9",          # 01, 1
        "Function_2_1FA",          # 02, 2
        "Function_3_EE7",          # 03, 3
        "Function_4_181B",         # 04, 4
        "Function_5_227F",         # 05, 5
        "Function_6_232A",         # 06, 6
        "Function_7_2377",         # 07, 7
        "Function_8_2391",         # 08, 8
        "Function_9_23AD",         # 09, 9
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_1EA")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1F8")
    OP_A3(0x2505)
    Event(0, 4)

    label("loc_1F8")

    Return()

    # Function_0_1C2 end

    def Function_1_1F9(): pass

    label("Function_1_1F9")

    Return()

    # Function_1_1F9 end

    def Function_2_1FA(): pass

    label("Function_2_1FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_425")
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x00◆Debug flag judgment (Walter part)\x01",
            "Regarding Walter battle in the Axis Pillar in SC\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[◇Defeated Walter with Zin in the party]\x01",         # 0
            "[◇Defeated Walter without Zin in the party]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_314"),
        (1, "loc_31A"),
        (SWITCH_DEFAULT, "loc_320"),
    )


    label("loc_314")

    OP_A2(0x2235)
    Jump("loc_320")

    label("loc_31A")

    OP_A3(0x2235)
    Jump("loc_320")

    label("loc_320")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x00◆Debug flag judgment (Luciola part)\x01",
            "Regarding Luciola battle in the Axis Pillar in SC\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[◇Defeated Luciola with Schera in the party]\x01",         # 0
            "[◇Defeated Luciola without Schera in the party]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_417"),
        (1, "loc_41D"),
        (SWITCH_DEFAULT, "loc_423"),
    )


    label("loc_417")

    OP_A2(0x2238)
    Jump("loc_423")

    label("loc_41D")

    OP_A3(0x2238)
    Jump("loc_423")

    label("loc_423")

    OP_56(0x0)

    label("loc_425")

    Sleep(500)
    OP_22(0x85, 0x3C, 0x64)
    OP_1D(0x1C)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Immediately after the collapse of the Aureole...\x02\x03",

            "Aboard a great ship cutting through the clouds...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_24(0x85, 0x46)
    Sleep(100)
    OP_24(0x85, 0x50)
    Sleep(100)
    OP_24(0x85, 0x5A)
    Sleep(100)
    OP_24(0x85, 0x64)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 5480, 0, -55430, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 3240, 0, -54970, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 3630, 0, -56800, 90)

    label("loc_510")

    OP_6F(0x1, 0)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6D(4710, 0, -11170, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(5100, 0)
    OP_6C(45000, 0)
    OP_6E(665, 0)

    def lambda_566():
        OP_6D(4680, 0, -52670, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_566)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(5130, 200, -54700, 0)
    OP_67(0, 5010, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(345, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x372D0, 0x69B68, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #3
        0x13,
        (
            "#230F#2POh, my... What a beautiful sight!\x02\x03",

            "The mystical land that we sought is crumbling\x01",
            "before our eyes!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_6BC")

    ChrTalk(    #4
        0x15,
        (
            "#250F#6PHeh heh... Suppose I could've seen this coming.\x02\x03",

            "Guess that means we lost this battle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_738")

    label("loc_6BC")


    ChrTalk(    #5
        0x15,
        (
            "#250F#6PBah. It was a battle we could've won, too.\x02\x03",

            "This is what all the professor's fault for getting\x01",
            "so out of hand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DF")

    ChrTalk(    #6
        0x14,
        (
            "#240F#4PAll returns to nothing...\x02\x03",

            "And once that flying city vanishes, our duty is\x01",
            "over as well.\x02\x03",

            "...It'll be time to say farewell again for a \x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87B")

    label("loc_7DF")


    ChrTalk(    #7
        0x13,
        (
            "#230F#2PAll returns to nothing...\x02\x03",

            "And once that flying city vanishes, our duty is\x01",
            "over as well.\x02\x03",

            "...It'll be time to say farewell again for a \x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")

    ChrTalk(    #8
        0x15,
        (
            "#250F#5P...\x02\x03",

            "Hmph. There's no guarantee we'll ever meet again\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_923")

    label("loc_8D8")


    ChrTalk(    #9
        0x15,
        (
            "#250F#6P...\x02\x03",

            "Hmph. There's no guarantee we'll ever meet again\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97C")
    OP_8C(0x14, 0, 400)
    Sleep(200)

    ChrTalk(    #10
        0x14,
        (
            "#240F#4POh?\x02\x03",

            "Are you considering leaving the society?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x15, 180, 400)
    Jump("loc_9F2")

    label("loc_97C")

    OP_8C(0x13, 270, 400)
    Sleep(200)

    ChrTalk(    #11
        0x13,
        (
            "#230F#2POh, my... What a peculiar thing to say.\x02\x03",

            "Are you considering leaving the society,\x01",
            "perchance?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(    #12
        0x15,
        (
            "#250F#5PWho knows? Even I don't know what the future\x01",
            "holds for me.\x02\x03",

            "Still, we Enforcers are the ones who decide our\x01",
            "own destinies.\x02\x03",

            "Which means what I do in the future is for me to\x01",
            "decide and no one else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA1")

    label("loc_ACF")


    ChrTalk(    #13
        0x15,
        (
            "#250F#6PWho knows? Even I don't know what the future\x01",
            "holds for me.\x02\x03",

            "Still, we Enforcers are the ones who decide our\x01",
            "own destinies.\x02\x03",

            "Which means what I do in the future is for me to\x01",
            "decide and no one else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA1")

    OP_8C(0x13, 270, 400)

    ChrTalk(    #14
        0x13,
        (
            "#230F#2PHmm... Quite so.\x02\x03",

            "Still, I believe it is only polite in these\x01",
            "circumstances to promise to meet again.\x02\x03",

            "To promise that one day, we will run into one\x01",
            "another on yet another battlefield somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB7")
    OP_8C(0x14, 0, 400)

    ChrTalk(    #15
        0x14,
        "#240F#4PHeehee. I suppose you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB7")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 5)), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(    #16
        0x15,
        (
            "#250F#6PHmph...\x02\x03",

            "Like there's any point in the 'battlefield' part.\x02\x03",

            "As if the lot of us would ever meet anywhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC5")

    label("loc_D3D")


    ChrTalk(    #17
        0x15,
        (
            "#250F#6PI suppose you're right.\x02\x03",

            "Still, it's not like our work will only be taking\x01",
            "place here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x13,
        (
            "#230F#2PHeh. Indeed.\x02\x03",

            "Well, then, as is custom, let us promise to meet\x01",
            "again.\x02\x03",

            "Until then, we must part ways.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E79")

    ChrTalk(    #19
        0x14,
        (
            "#240F#4PIndeed. Let us meet again.\x02\x03",

            "Wherever and however destiny would have us meet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC5")

    label("loc_E79")


    ChrTalk(    #20
        0x15,
        (
            "#250F#6PYeah.\x02\x03",

            "See ya all on another bloody battlefield one day,\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC5")

    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1FA end

    def Function_3_EE7(): pass

    label("Function_3_EE7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_72(0x802, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    OP_C4(0x0, 0x10)
    OP_48()
    FadeToBright(1, 0)
    OP_1D(0xD4)
    Sleep(500)
    PlayMovie(0x0, "ED6_DT50.dat", 0x0, 0x1)
    Sleep(1000)
    OP_56(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    LoadEffect(0x1, "map\\\\mp303_00.eff")
    OP_22(0x85, 0x1, 0xA)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x32)
    OP_22(0x131, 0x1, 0x14)
    Sleep(200)
    OP_24(0x85, 0x3C)
    OP_24(0x131, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x46)
    OP_24(0x131, 0x28)
    Sleep(200)
    OP_24(0x85, 0x50)
    OP_24(0x131, 0x32)
    Sleep(200)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 7600, 0, -55320, 87)
    SetChrChipByIndex(0x13, 2)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 7600, 0, -56500, 270)
    SetChrChipByIndex(0x15, 5)
    SetChrSubChip(0x15, 0)
    OP_6F(0x1, 0)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6D(0, 200, -21020, 0)
    OP_67(0, 13020, -10000, 0)
    OP_6B(5100, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)

    def lambda_1091():
        OP_6D(8320, 200, -56180, 9000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1091)

    def lambda_10A9():
        OP_67(0, 7280, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_10A9)

    def lambda_10C1():
        OP_6C(58000, 9000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_10C1)

    def lambda_10D1():
        OP_6E(465, 9000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_10D1)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Fade(500)
    OP_11(0xFF, 0xFF, 0xFF, 0x372D0, 0x69B68, 0x0)
    OP_6D(8500, 200, -55800, 0)
    OP_67(0, 4480, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(68000, 0)
    OP_6E(344, 0)
    OP_8C(0x13, 135, 0)
    OP_0D()

    def lambda_114A():
        OP_6B(2420, 30000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_114A)
    Sleep(1000)

    ChrTalk(    #21
        0x13,
        "#232F#5P#30W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x15,
        (
            "#257F#6P#30W...\x02\x03",

            "#255FHey, Bleublanc.\x02\x03",

            "Don't just stand there. Say something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#231F#5P#30WHeh. Why should I be the one to break the silence?\x02\x03",

            "#230FWords have no meaning in the face of such an\x01",
            "splendorous sight.\x02\x03",

            "All there is for us to do is to be overwhelmed\x01",
            "and awed by the spectacle before us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x15,
        "#256F#6P#30W...Bah.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x15)
    Sleep(500)

    ChrTalk(    #25
        0x15,
        (
            "#257F#6P#30WThe others still haven't come back, either.\x02\x03",

            "#253FKinda crummy ending to this whole schtick, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x13,
        (
            "#232F#5P#30WRenne left the city and has since departed this\x01",
            "region.\x02\x03",

            "Luciola is missing...but no good can come from\x01",
            "us fretting for her safety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x15,
        (
            "#252F#6P#30WHeh. Oh, no worries on that front.\x02\x03",

            "#250FJust think it'd be a waste for a woman like\x01",
            "her to die so early.\x02\x03",

            "So, you know. Here's hopin' she didn't lose\x01",
            "her life for nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x13,
        (
            "#231F#5P#30WHah. I quite agree.\x02\x03",

            "#232FAs for Loewe...I fear the odds of him\x01",
            "making it out alive are nonexistent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x15,
        (
            "#257F#6P#30W...Yeah.\x02\x03",

            "#256FDamn it... If I'd known this was gonna happen,\x01",
            "I would've finally made him fight me.\x02\x03",

            "He was always finding excuses to get out of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#230F#5P#30WWell, unlike us, he had a clear and specific\x01",
            "purpose for taking part in all of this.\x02\x03",

            "And it looks like he may well have been able\x01",
            "to achieve it, at that.\x02\x03",

            "Though he met his end, I have an inkling that\x01",
            "he, at least, is satisfied by the ending to this\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x15,
        "#257F#6P#30WBlech...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_16F7():
        OP_6B(2320, 3000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_16F7)

    def lambda_1707():
        OP_99(0xFE, 0x0, 0x6, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1707)
    WaitChrThread(0x15, 0x2)
    OP_22(0x2E4, 0x0, 0x46)
    PlayEffect(0x1, 0x0, 0x15, -200, 100, -150, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    OP_22(0x2E5, 0x0, 0x64)
    OP_82(0x0, 0x2)

    def lambda_1763():
        OP_99(0xFE, 0x6, 0x8, 0x320)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1763)
    WaitChrThread(0x15, 0x2)
    Sleep(1500)
    PlayEffect(0x1, 0x0, 0x15, -350, 100, -80, 0, 0, 0, 600, 700, 600, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #32
        0x15,
        "#254F#5P#30WHard to believe it's all over.\x02",
    )

    CloseMessageWindow()

    def lambda_17E7():
        OP_6D(16000, 200, -55800, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_17E7)
    FadeToDark(3000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_3_EE7 end

    def Function_4_181B(): pass

    label("Function_4_181B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x124, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1020, 150, -14080, 180)
    SetChrPos(0x10, 4550, 0, -32170, 270)
    OP_A1(0x10, 0x4)
    ClearChrFlags(0x10, 0x1)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x401, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x0)
    OP_6D(-1910, 14950, -20340, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(45000, 0)
    OP_6E(405, 0)

    def lambda_18F1():
        OP_6D(3040, 0, -18590, 6000)
        ExitThread()

    QueueWorkItem(0x124, 0, lambda_18F1)

    def lambda_1909():
        OP_67(0, 4960, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x124, 1, lambda_1909)

    def lambda_1921():
        OP_6B(2550, 6000)
        ExitThread()

    QueueWorkItem(0x124, 2, lambda_1921)

    def lambda_1931():
        OP_6E(405, 6000)
        ExitThread()

    QueueWorkItem(0x124, 3, lambda_1931)
    OP_11(0xFF, 0xFF, 0xFF, 0x50140, 0x68BC8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    OP_22(0x133, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xE6)
    Sleep(2000)

    def lambda_1978():
        OP_8F(0xFE, 0x474, 0x96, 0xFFFFAE20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1978)
    WaitChrThread(0x12, 0x0)
    OP_73(0x1)
    WaitChrThread(0x124, 0x0)
    Sleep(1000)
    OP_43(0x12, 0x0, 0x0, 0x8)
    Sleep(2000)
    Fade(1000)
    OP_6D(8720, 0, -33830, 0)
    OP_67(0, 3940, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(113000, 0)
    OP_6E(418, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x64578, 0x68BC8, 0x0)
    OP_72(0x404, 0x0)
    ExitThread()
    SetChrFlags(0x10, 0x1)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x12,
        (
            "#120F#5PHeh. These things truly are monstrous.\x02\x03",

            "Still, given that our destination is a monstrous\x01",
            "ancient prison...\x02\x03",

            "Perhaps that is the most fitting way for its\x01",
            "vanguards to be.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1AD5():
        OP_6D(6410, 2500, -33810, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1AD5)

    def lambda_1AED():
        OP_67(0, 4110, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AED)

    def lambda_1B05():
        OP_6B(2940, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1B05)

    def lambda_1B15():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_1B15)
    Sleep(500)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x1)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 1)
    Sleep(500)
    SetChrSubChip(0x12, 2)
    OP_7D(0x0, 0x12, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1B64():
        OP_96(0xFE, 0x12C0, 0x12C0, 0xFFFF810C, 0x157C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1B64)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 180, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x12, 0x4)
    SetChrSubChip(0x12, 1)
    OP_CF(0x12, 0x4, "Frame143_on_head")
    OP_7D(0x1, 0x12, 0x0, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Sleep(500)
    OP_8C(0x12, 0, 400)
    Sleep(1000)
    Fade(300)
    SetChrChipByIndex(0x12, 0)
    SetChrSubChip(0x12, 1)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(1000)
    LoadEffect(0x0, "monster\\ms30803a.eff")
    LoadEffect(0x1, "monster\\ms30803b.eff")
    LoadEffect(0x2, "map\\mp021_00.eff")
    OP_22(0xF3, 0x0, 0x64)
    Fade(300)
    PlayEffect(0x0, 0x0, 0x10, 0, 3300, 900, 0, -4, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    Fade(300)
    OP_82(0x0, 0x2)
    OP_0D()
    Sleep(500)
    OP_D8(0x4, 0x1F4)
    OP_43(0x10, 0x3, 0x0, 0x7)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 845)
    OP_70(0x4, 0x361)

    def lambda_1CB1():
        OP_8F(0xFE, 0x3B6, 0x0, 0xFFFF840E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1CB1)
    Sleep(1000)
    Fade(1000)
    OP_11(0xFF, 0xFF, 0xFF, 0x64578, 0xC3500, 0x0)
    OP_6D(780, -2700, -25780, 0)
    OP_67(0, 4170, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(0, 0)
    OP_6E(510, 0)

    def lambda_1D23():
        OP_6D(780, -4000, -27780, 7500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1D23)

    def lambda_1D3B():
        OP_67(0, 4000, -10000, 7500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1D3B)

    def lambda_1D53():
        OP_6B(4500, 7500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_1D53)
    Sleep(1000)

    def lambda_1D68():
        OP_8C(0xFE, 180, 60)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1D68)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x10, 0x1)
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_73(0x4)
    OP_D8(0x4, 0x1F4)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_6F(0x4, 0)
    OP_70(0x4, 0x14)
    Sleep(500)
    OP_44(0x10, 0x3)
    OP_23(0xEC)
    Sleep(500)
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_73(0x4)
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 140)
    OP_70(0x4, 0x95)
    OP_73(0x4)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x12, 0x3)
    Fade(500)
    OP_6D(-3500, 500, -60560, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(272000, 0)
    OP_6E(544, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x61A80, 0x829D8, 0x0)

    def lambda_1E2E():

        label("loc_1E2E")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1E2E")

    QueueWorkItem2(0x12, 3, lambda_1E2E)
    OP_22(0x85, 0x1, 0x50)

    def lambda_1E4E():
        OP_6D(-3500, 500, -30000, 2000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1E4E)
    Play3DEffect(0x1, 0x1, 0x4, "Frame80_Bone__79_", 0x190, 0x0, 0x708, 0xFFF1, 0x10E, 0xB4, 0x7D0, 0x7D0, 0x4B0, 0x0)
    Play3DEffect(0x1, 0x2, 0x4, "Frame83_Bone__82_", 0xFFFFFE70, 0x0, 0x708, 0xFFE7, 0x10E, 0xB4, 0x7D0, 0x7D0, 0x4B0, 0x0)
    OP_22(0x113, 0x1, 0x64)
    PlayEffect(0x2, 0x3, 0x10, 0, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x114, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x12, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2000, 0, -39590, 0)
    OP_67(0, 4830, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(212000, 0)
    OP_6E(599, 0)
    OP_0D()

    def lambda_1F6D():

        label("loc_1F6D")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1F6D")

    QueueWorkItem2(0x12, 3, lambda_1F6D)

    ChrTalk(    #34
        0x12,
        (
            "#120F#5PGo forth, jet-black wings!\x02\x03",

            "Let the fools of the world know the truth!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FDC():

        label("loc_1FDC")

        OP_7C(0x50, 0x50, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1FDC")

    QueueWorkItem2(0x12, 3, lambda_1FDC)
    Sleep(1000)
    OP_82(0x3, 0x2)
    OP_23(0xCC)
    OP_B0(0x4, 0x14)
    OP_6F(0x4, 150)
    OP_70(0x4, 0xC8)
    Sleep(500)
    Play3DEffect(0x1, 0x1, 0x4, "Frame80_Bone__79_", 0x190, 0x0, 0x708, 0xFFF1, 0x10E, 0xB4, 0xFA0, 0xFA0, 0xDAC, 0x0)
    Play3DEffect(0x1, 0x2, 0x4, "Frame83_Bone__82_", 0xFFFFFE70, 0x0, 0x708, 0xFFE7, 0x10E, 0xB4, 0xFA0, 0xFA0, 0xDAC, 0x0)
    Sleep(200)

    def lambda_208E():
        OP_91(0xFE, 0x0, 0x1388, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_208E)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(200)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(730, 0, -62900, 0)
    OP_67(0, 7680, -10000, 0)
    OP_6B(10860, 0)
    OP_6C(56000, 0)
    OP_6E(560, 0)
    OP_71(0x404, 0x0)
    ExitThread()
    SetChrPos(0x11, 0, 5000, -60000, 0)
    OP_A1(0x11, 0x3)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_8C(0x11, 180, 0)
    OP_D1(17, -45000, 150000, 15000, 0)
    OP_CF(0x12, 0x3, "Frame134_on_head")
    OP_71(0x2003, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 320)
    OP_70(0x3, 0x154)

    def lambda_216D():

        label("loc_216D")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_216D")

    QueueWorkItem2(0x12, 3, lambda_216D)

    def lambda_2188():
        OP_6B(16460, 8000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2188)
    OP_43(0x12, 0x1, 0x0, 0x5)
    OP_43(0x11, 0x3, 0x0, 0x6)
    OP_98(0x0, 0x11)
    OP_98(0x1, 0xFFFFB1E0, 0x7530, 0xFFFEA840)
    OP_98(0x1, 0xFFFF15A0, 0xC350, 0xFFFEEE90)
    OP_98(0x1, 0xFFFE2B40, 0x1ADB0, 0xFFFD8F00)

    def lambda_21D4():
        OP_98(0x2, 0xFE, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_21D4)
    Sleep(6500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x10, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2272")
    Sleep(1000)
    OP_28(0x10, 0x4, 0x10)
    OP_28(0x10, 0x4, 0x20)
    OP_3E(0x2EA, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05Received \x1F\xEA\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(4000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #36
        "\x07\x05Received \x07\x024,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2272")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5402   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_4_181B end

    def Function_5_227F(): pass

    label("Function_5_227F")

    OP_24(0x113, 0x32)
    OP_24(0x114, 0x32)
    Sleep(500)
    OP_24(0x113, 0x3C)
    OP_24(0x114, 0x3C)
    Sleep(500)
    OP_24(0x113, 0x46)
    OP_24(0x114, 0x46)
    Sleep(500)
    OP_24(0x113, 0x50)
    OP_24(0x114, 0x5A)
    Sleep(500)

    def lambda_22B9():

        label("loc_22B9")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_22B9")

    QueueWorkItem2(0x12, 3, lambda_22B9)
    OP_24(0x113, 0x64)
    OP_24(0x114, 0x64)
    Sleep(3500)
    OP_24(0x113, 0x5A)
    OP_24(0x114, 0x5A)
    Sleep(500)
    OP_24(0x113, 0x4B)
    OP_24(0x114, 0x4B)
    Sleep(400)
    OP_24(0x113, 0x32)
    OP_24(0x114, 0x32)
    Sleep(300)
    OP_24(0x113, 0x19)
    OP_24(0x114, 0x19)
    Sleep(200)
    OP_24(0x113, 0x0)
    OP_24(0x114, 0x0)
    Sleep(100)
    OP_23(0x113)
    OP_23(0x114)
    OP_23(0x85)
    OP_44(0x12, 0x3)
    Return()

    # Function_5_227F end

    def Function_6_232A(): pass

    label("Function_6_232A")

    OP_D1(254, -150000, 150000, 30000, 800)
    OP_D1(254, -150000, 130000, 220000, 800)
    OP_D1(254, -10000, 170000, 310000, 500)
    OP_D1(254, -20000, 180000, 345000, 1500)
    Return()

    # Function_6_232A end

    def Function_7_2377(): pass

    label("Function_7_2377")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2390")
    OP_22(0xEC, 0x0, 0x64)
    Sleep(700)
    OP_23(0xEC)
    Jump("Function_7_2377")

    label("loc_2390")

    Return()

    # Function_7_2377 end

    def Function_8_2391(): pass

    label("Function_8_2391")

    OP_8F(0xFE, 0x19A, 0x0, 0xFFFF897C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_2391 end

    def Function_9_23AD(): pass

    label("Function_9_23AD")

    OP_8F(0xFE, 0x11C6, 0xC350, 0xFFFF7A86, 0x1388, 0x0)
    Return()

    # Function_9_23AD end

    SaveToFile()

Try(main)
