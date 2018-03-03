from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2811   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2811.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Deborah',                              # 9
        'Ricky',                                # 10
        'Lucy',                                 # 11
        'Target Camera',                        # 12
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
        'ED6_DT07/CH01130 ._CH',             # 00
        'ED6_DT26/CH20783 ._CH',             # 01
        'ED6_DT07/CH02690 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01130P._CP',             # 00
        'ED6_DT26/CH20783P._CP',             # 01
        'ED6_DT07/CH02690P._CP',             # 02
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -4900,
        Z                   = 140,
        Y                   = -4650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 30860,
        Z                   = 0,
        Y                   = 57160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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


    DeclActor(
        TriggerX            = 29620,
        TriggerZ            = 0,
        TriggerY            = 60000,
        TriggerRange        = 1000,
        ActorX              = 29620,
        ActorZ              = 1500,
        ActorY              = 60000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1A6",          # 01, 1
        "Function_2_1A7",          # 02, 2
        "Function_3_324",          # 03, 3
        "Function_4_329",          # 04, 4
        "Function_5_4BE",          # 05, 5
        "Function_6_5FF",          # 06, 6
        "Function_7_8D9",          # 07, 7
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_1A5")

    Return()

    # Function_0_18A end

    def Function_1_1A6(): pass

    label("Function_1_1A6")

    Return()

    # Function_1_1A6 end

    def Function_2_1A7(): pass

    label("Function_2_1A7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_30E")

    label("loc_1CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_30E")

    label("loc_1E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_30E")

    label("loc_1FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_30E")

    label("loc_217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_30E")

    label("loc_230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_30E")

    label("loc_249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_262")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_30E")

    label("loc_262")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_30E")

    label("loc_27B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_30E")

    label("loc_294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_30E")

    label("loc_2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_30E")

    label("loc_2C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_30E")

    label("loc_2DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_30E")

    label("loc_2F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_30E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_323")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_30E")

    label("loc_323")

    Return()

    # Function_2_1A7 end

    def Function_3_324(): pass

    label("Function_3_324")

    Call(0, 4)
    Return()

    # Function_3_324 end

    def Function_4_329(): pass

    label("Function_4_329")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_4BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F1")

    ChrTalk(    #0
        0x10,
        (
            "Maybe it's just me, but you're looking a little\x01",
            "blue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "We're open until late if you're feeling hungry.\x01",
            "Sometimes a good meal is just what you need\x01",
            "to cheer right back up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA")

    label("loc_3F1")


    ChrTalk(    #2
        0x10,
        (
            "One of the girls in the Student Council has been\x01",
            "working awfully late today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "We're open till late, though, so I hope she'll\x01",
            "come down here if she's feeling hungry.\x01",
            "That goes for you, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4BA")

    TalkEnd(0x10)
    Return()

    # Function_4_329 end

    def Function_5_4BE(): pass

    label("Function_5_4BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_5FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #4
        0xFE,
        "Being a student isn't so bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Like, how many places can you think of that'll\x01",
            "give you good food that's actually AFFORDABLE?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB")

    label("loc_558")


    ChrTalk(    #6
        0xFE,
        "*munch* This is sooo good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I decided to have a nap after class was over,\x01",
            "and before I knew it, the sun was down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "So here I am, having my dinner.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5FB")

    TalkEnd(0xFE)
    Return()

    # Function_5_4BE end

    def Function_6_5FF(): pass

    label("Function_6_5FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_8D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 2)), scpexpr(EXPR_END)), "loc_68F")

    ChrTalk(    #9
        0x12,
        (
            "#1790FYou should probably head back to your room\x01",
            "soon if you've got no reason to be out.\x02\x03",

            "It's past curfew, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D5")

    label("loc_68F")


    ChrTalk(    #10
        0x105,
        (
            "#043FI didn't know you were here, Lucy.\x02\x03",

            "Are you still working? It's awfully late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x12,
        (
            "#1790FI was, yes... It took me a bit longer than\x01",
            "I'd expected to finish everything.\x02\x03",

            "I'm almost done, though, so I'll head back\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        "#049FO-Oh. That's good...\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x12,
        (
            "#1792FIs something wrong, Kloe?\x02\x03",

            "You seem kind of down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#047FNo... I'm all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x12,
        (
            "#1794FWell, if you say so...\x02\x03",

            "#1790FIt's past curfew, though. You should probably\x01",
            "start heading back to your room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        (
            "#043FI suppose...\x02\x03",

            "#049F(That's the last place I want to be right now...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7A)

    label("loc_8D5")

    TalkEnd(0xFE)
    Return()

    # Function_6_5FF end

    def Function_7_8D9(): pass

    label("Function_7_8D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_9F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 1)), scpexpr(EXPR_END)), "loc_957")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Climb Up\x01",         # 0
            "Don't Climb\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_954")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2800   ._SN", 130, 0, 0)
    IdleLoop()
    Jump("loc_954")

    label("loc_954")

    Jump("loc_9F8")

    label("loc_957")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05There's a rope hanging down outside the window.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #18
        0x105,
        (
            "#047F...\x02\x03",

            "I think I could climb up there if I used this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F81)

    label("loc_9F8")

    TalkEnd(0xFF)
    Return()

    # Function_7_8D9 end

    SaveToFile()

Try(main)
