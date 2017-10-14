from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1500   ._SN',
        MapName             = 'Bose',
        Location            = 'R1500.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        'Red-Haired Guy',                       # 9
        'Ravennue Village',                     # 10
        'West Bose Highway',                    # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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
        Unknown_3A              = 59,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT06/CH20053 ._CH',             # 00
        'ED6_DT09/CH10030 ._CH',             # 01
        'ED6_DT09/CH10031 ._CH',             # 02
        'ED6_DT09/CH10330 ._CH',             # 03
        'ED6_DT09/CH10331 ._CH',             # 04
        'ED6_DT09/CH10310 ._CH',             # 05
        'ED6_DT09/CH10310 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT06/CH20053P._CP',             # 00
        'ED6_DT09/CH10030P._CP',             # 01
        'ED6_DT09/CH10031P._CP',             # 02
        'ED6_DT09/CH10330P._CP',             # 03
        'ED6_DT09/CH10331P._CP',             # 04
        'ED6_DT09/CH10310P._CP',             # 05
        'ED6_DT09/CH10310P._CP',             # 06
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 0,
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
        X                   = -170710,
        Z                   = 12010,
        Y                   = 95390,
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

    DeclNpc(
        X                   = -204960,
        Z                   = -100,
        Y                   = -46530,
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


    DeclMonster(
        X                   = -191470,
        Z                   = 3990,
        Y                   = 18830,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180300,
        Z                   = 3990,
        Y                   = -3330,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -166330,
        Z                   = 11950,
        Y                   = 8590,
        Unknown_0C          = 0,
        Unknown_0E          = 1,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -210250,
        Y                   = -5000,
        Z                   = -8632,
        Range               = -197450,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFD3FA,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1B7",          # 01, 1
        "Function_2_1CA",          # 02, 2
        "Function_3_1E0",          # 03, 3
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Return()

    # Function_0_1B6 end

    def Function_1_1B7(): pass

    label("Function_1_1B7")

    OP_16(0x2, 0xFA0, 0xFFFB6C20, 0xFFFE6DA8, 0x3001F)
    Return()

    # Function_1_1B7 end

    def Function_2_1CA(): pass

    label("Function_2_1CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1CA")

    label("loc_1DF")

    Return()

    # Function_2_1CA end

    def Function_3_1E0(): pass

    label("Function_3_1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_127C")
    OP_A2(0x319)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0x8, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -192020, 3600, 10030, 223)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")

    ChrTalk(    #0
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F")

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")

    ChrTalk(    #1
        0x102,
        "#014FHuh...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28F")

    label("loc_271")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28F")

    ChrTalk(    #2
        0x103,
        "#023FHmm...?\x02",
    )

    CloseMessageWindow()

    label("loc_28F")


    def lambda_295():
        OP_6D(-197690, 1800, 1790, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_295)

    def lambda_2AD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2AD)
    Sleep(500)

    def lambda_2C2():
        OP_8E(0xFE, 0xFFFCFF9A, 0x802, 0xB40, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2C2)
    Sleep(2000)
    WaitChrThread(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #3
        0x8,
        "Red-Haired Guy",
        "#052FOh...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x103, -205000, 1920, -8810, 22)
    SetChrPos(0x101, -205000, 1920, -8810, 22)
    SetChrPos(0x102, -205000, 1920, -8810, 22)

    def lambda_355():
        OP_8E(0xFE, 0xFFFCFB62, 0x802, 0xFFFFFF88, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_355)
    Sleep(500)

    def lambda_375():
        OP_8E(0xFE, 0xFFFCF3EC, 0x79E, 0xFFFFFFD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_375)
    Sleep(500)

    def lambda_395():
        OP_8E(0xFE, 0xFFFCF3A6, 0x7D9, 0xFFFFF920, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_395)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 0)
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 0)

    NpcTalk(    #4
        0x8,
        "Red-Haired Guy",
        (
            "#050FScherazard, is that you? Well, this\x01",
            "is an unlikely place to run into the\x01",
            "'Silver Streak'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x103,
        (
            "#020FRight back at you.\x02\x03",

            "I thought you were in the Royal\x01",
            "City, but are you here to look\x01",
            "into the airliner incident?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #6
        0x8,
        "Red-Haired Guy",
        (
            "#053FNo, I'm here on some chump\x01",
            "errands...\x02\x03",

            "#050FBut speaking of the incident,\x01",
            "I hear it was the work of the\x01",
            "sky bandits.\x02\x03",

            "Still, if you're here on the job\x01",
            "then I guess I don't have to worry\x01",
            "about it myself.\x02\x03",

            "Good luck to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#022FIs that all you've got to say?\x02\x03",

            "I'm sure you've heard that Cassius\x01",
            "might have been taken hostage,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x8,
        "Red-Haired Guy",
        (
            "#052F#051FCassius Bright? Taken hostage?\x02\x03",

            "Ha ha ha, don't make me laugh!\x02\x03",

            "That old man's not going to get\x01",
            "beaten by the likes of some\x01",
            "sky bandits!\x02\x03",

            "Anybody saying that is severely\x01",
            "mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        "#025FI'd like to believe that too, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#002F(I wonder who this guy is...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010F(I don't know...but he seems\x01",
            "to fit the mold for a bracer.)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #12
        0x8,
        "Red-Haired Guy",
        (
            "#050FBy the way...who are those brats\x01",
            "you've got tagging along with you?\x02\x03",

            "They look like a bunch of newbies\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#021FHa ha. Well, then I'm sure you'll\x01",
            "be surprised to hear that these\x01",
            "brats...\x02\x03",

            "...are Cassius' kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #14
        0x8,
        "Red-Haired Guy",
        (
            "#052FYeah, that's a surprise, all right...\x01",
            "So these are the old man's kids,\x01",
            "huh?\x02\x03",

            "Hmm...\x01",
            "Hard to believe it...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFCFA54, 0x7ED, 0x58C, 0x7D0, 0x0)

    NpcTalk(    #15
        0x8,
        "Red-Haired Guy",
        "#057F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#004FWh-Why're you looking at us\x01",
            "like that...?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x8,
        "Red-Haired Guy",
        (
            "#050FThis boy with the black hair is one\x01",
            "thing...but the girl really looks like\x01",
            "an amateur.\x02\x03",

            "#050FAre you sure she's really Cassius'\x01",
            "daughter?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x101,
        (
            "#005FYou wanna try saying that again\x01",
            "with my staff in your teeth?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FShe's the bona fide daughter of Cassius\x01",
            "Bright, and I have to warn you, her bite\x01",
            "is as good as her bark.\x02\x03",

            "And I'm just his adopted son.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #20
        0x8,
        "Red-Haired Guy",
        (
            "#052FIs that a fact?\x02\x03",

            "#053FOh well, it doesn't really matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#009FWhat do you mean 'it doesn't\x01",
            "matter'?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    NpcTalk(    #22
        0x8,
        "Red-Haired Guy",
        (
            "#051F#3PWell, take it easy, Scherazard.\x02\x03",

            "And be careful not to let these\x01",
            "brats drag you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#027FYeah, yeah.\x02\x03",

            "And make sure not to rush into\x01",
            "any trouble yourself, either.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x8,
        "Red-Haired Guy",
        (
            "#051F#3PHa ha, I'll keep those words\x01",
            "in mind.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E0D")

    ChrTalk(    #25
        0x8,
        (
            "#050F#3POh, right, Scherazard.\x02\x03",

            "Was it you who took care of\x01",
            "that monster near the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#020FYeah.\x02\x03",

            "Well, actually, it wasn't just me--\x01",
            "it was us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "#053F#3PHa, I don't think any number of\x01",
            "trainees would have made much\x01",
            "difference.\x02\x03",

            "#053F...\x02\x03",

            "#051FBut anyway, good luck in your\x01",
            "search for those sky bandits.\x02\x03",

            "Later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0D")


    def lambda_E13():

        label("loc_E13")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E13")

    QueueWorkItem2(0x101, 2, lambda_E13)

    def lambda_E24():

        label("loc_E24")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E24")

    QueueWorkItem2(0x102, 2, lambda_E24)

    def lambda_E35():

        label("loc_E35")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_E35")

    QueueWorkItem2(0x103, 2, lambda_E35)

    def lambda_E46():
        OP_6D(-198470, 2000, 160, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E46)
    OP_8E(0x8, 0xFFFCF342, 0x7B2, 0x500, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFCEF28, 0x73A, 0xC8, 0xBB8, 0x0)
    OP_8E(0x8, 0xFFFCE9D8, 0x730, 0xFFFFDB20, 0xBB8, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)

    ChrTalk(    #28
        0x101,
        (
            "#005F#1PWh-What's with that guy?!\x02\x03",

            "He really pisses me off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010F#1PI see...so that was 'Heavy Blade Agate',\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#004F#1P'Heavy Blade Agate'?\x01",
            "What a stupid name...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #31
        0x103,
        (
            "#020FAgate Crosner. Senior bracer in\x01",
            "the Bracer Guild.\x02\x03",

            "#020FHe works in all regions and isn't\x01",
            "affiliated with any specific branch.\x02\x03",

            "His massive blade is said to be\x01",
            "capable of slicing a monster in\x01",
            "two with a single slash.\x02\x03",

            "I'll just tell you right now,\x01",
            "he's one tough customer.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #32
        0x101,
        (
            "#009FWhatever. I don't care how tough\x01",
            "he is. He's still a rude jerk.\x02\x03",

            "Come to think of it, how does he\x01",
            "know Dad anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 45, 400)

    ChrTalk(    #33
        0x102,
        (
            "#010F#1PHe seems to think highly of Dad's\x01",
            "ability, but even so, he didn't seem\x01",
            "to like him all that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        (
            "#026FThere are a number of things in\x01",
            "his past I can't go into...\x02\x03",

            "And those things are the reason\x01",
            "why he feels that way about your\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#002FHmm...\x02\x03",

            "Well, I couldn't care less about\x01",
            "someone rude like that.\x02\x03",

            "Anyway, let's hurry to Ravennue\x01",
            "Village!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_127C")

    Return()

    # Function_3_1E0 end

    SaveToFile()

Try(main)
